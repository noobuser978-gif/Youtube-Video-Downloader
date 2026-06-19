import os
import yt_dlp
import yt_dlp.utils
from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home(request: Request):
    try:
        with open("templates/index.html") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Frontend template index.html not found.")


@app.post("/echo")
def echo(url: str = Form(...)):
    print(f"Received: {url}")
    return {"received": url}


@app.post("/video-info")
def video_info(url: str = Form(...)):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'force_generic_extractor': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            formats = []
            for f in info.get('formats', []):
                if f.get('height') and f.get('ext') in ['mp4', 'webm']:
                    formats.append({
                        'format_id': f['format_id'],
                        'height': f.get('height'),
                        'ext': f.get('ext'),
                        'filesize': f.get('filesize', 0),
                        'has_video': True,
                        'has_audio': True,
                        'quality': f"{f.get('height')}p"
                    })
                elif f.get('acodec') != 'none' and f.get('vcodec') == 'none':
                    formats.append({
                        'format_id': f['format_id'],
                        'ext': 'mp3',
                        'filesize': f.get('filesize', 0),
                        'has_video': False,
                        'has_audio': True,
                        'quality': 'Audio Only'
                    })

            return {
                "success": True,
                "title": info.get('title', 'Unknown'),
                "duration": info.get('duration', 0),
                "thumbnail": info.get('thumbnail', ''),
                "channel": info.get('channel', info.get('uploader', 'Unknown')),
                "formats": formats[:10]
            }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/download")
def download_video(url: str = Form(...), format_id: str = Form("best"), media_type: str = Form("video")):
    DOWNLOAD_DIR = "downloads"
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    outtmpl_path = os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')

    if media_type == "audio":
        ydl_opts = {
            'outtmpl': outtmpl_path,
            'quiet': True,
            'no_warnings': True,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
        }
    else:
        ydl_opts = {
            'outtmpl': outtmpl_path,
            'quiet': True,
            'no_warnings': True,
            'format': format_id if format_id != "best" else "bestvideo+bestaudio/best",
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

            if media_type == "audio":
                filename = filename.rsplit('.', 1)[0] + '.mp3'

            just_filename = os.path.basename(filename)

        return {
            "success": True,
            "message": "Download complete",
            "filename": just_filename
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
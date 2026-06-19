# 🎬 YouTube Video Downloader

A lightweight, web-based YouTube downloader built with FastAPI and yt-dlp. Download videos and audio with a clean, modern interface.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-teal.svg)

---

## 📌 Overview

This tool provides a simple web interface to download YouTube videos and audio. Paste a URL, choose your quality, and download instantly.

**Key Features:**
- Download video in multiple qualities (720p, 480p, 360p)
- Extract audio as MP3
- Real-time progress indicator
- Clean, responsive dark theme

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [FFmpeg](https://ffmpeg.org/) (required for audio extraction)

**Install FFmpeg:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows - Download from ffmpeg.org
```
## Installation
```bash
# Clone the repository
git clone https://github.com/noobuser978-gif/Youtube-Video-Downloader
cd youtube-downloader

# Install dependencies
pip install -r requirements.txt
```

## Run the Application
```bash
python app.py
```
Open your browser and visit: http://127.0.0.1:8000

## 📖 How to Use
1. Paste the Youtube URL into the input field
2. Click Fetch or press Enter
3. Select your preferred quality from the list
4. Click Download to save the file
   
All downloads are saved to the /downloads folder

## 🙋 Support

   Author: Rajbir Yadav
   
   Email: noobuser978@gmail.com
   
   GitHub: noobuser978-gif

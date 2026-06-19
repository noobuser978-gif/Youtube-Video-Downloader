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

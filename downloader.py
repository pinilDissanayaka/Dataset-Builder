import subprocess
import os
from config import RAW_AUDIO_DIR

def download_podcast(youtube_url: str):
    os.makedirs(RAW_AUDIO_DIR, exist_ok=True)

    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "wav",
        "--audio-quality", "0",
        "--yes-playlist",
        "-o", f"{RAW_AUDIO_DIR}/%(title)s.%(ext)s",
        youtube_url
    ]
    subprocess.run(cmd, check=True)

import os


INPUT_DIR = "media"
OUTPUT_DIR = "transcriptions"

# Supported media file types
AUDIO_EXTENSIONS = (".mp3", ".wav", ".m4a", ".flac")
VIDEO_EXTENSIONS = (".mp4", ".avi", ".mov", ".mkv", ".webm")


WHISPER_MODEL = "tiny"


os.makedirs(OUTPUT_DIR, exist_ok=True)

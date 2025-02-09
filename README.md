📜 README for Whisper Transcription Project
🎤 Whisper Media Transcription Project

A Python-based transcription tool that automatically scans a directory for audio & video files, transcribes them using OpenAI's Whisper, and saves the results in text & JSON format.
🚀 Features

✅ Recursively scans folders to find media files
✅ Supports audio & video formats (MP3, WAV, MP4, etc.)
✅ Converts non-WAV files for better transcription accuracy
✅ Uses Whisper (tiny model) for fast transcription
✅ Saves transcriptions in structured JSON & text format
✅ Easy to extend & customize
🛠 Installation
1️⃣ Install Dependencies

Make sure you have Python 3 installed, then run:

pip install openai-whisper ffmpeg pydub

Also, install FFmpeg:

sudo apt install ffmpeg  # Ubuntu/Linux
brew install ffmpeg      # macOS

📁 Project Structure

📂 media_transcription_project/
 ├── 📂 src/                 # Source code directory
 │   ├── __init__.py         # Marks src as a package
 │   ├── config.py           # Configuration settings
 │   ├── file_parser.py      # Handles folder parsing
 │   ├── transcriber.py      # Transcribes media files
 │   ├── output_manager.py   # Saves results to text & JSON
 │   ├── main.py             # Main script to run the program
 ├── 📂 media/               # Place input media files here
 ├── 📂 transcriptions/      # Output transcriptions
 ├── requirements.txt        # Required Python packages
 ├── README.md               # Documentation

🎯 How to Use
1️⃣ Place Media Files

Put your audio & video files inside the media/ folder.
2️⃣ Run the Transcription Script

python3 src/main.py

3️⃣ View Transcriptions

After running the script, transcriptions will be saved in transcriptions/:

📂 transcriptions/
 ├── audio1.json
 ├── audio1.txt
 ├── video1.json
 ├── video1.txt

Example JSON Output:

{
    "file": "media/audio1.mp3",
    "transcription": "Hello, this is an example transcription."
}

📝 Customization

    Change the Whisper model in config.py:

WHISPER_MODEL = "tiny"

Options: "tiny", "base", "small", "medium", "large"

Modify supported file types in config.py:

AUDIO_EXTENSIONS = (".mp3", ".wav", ".m4a", ".flac")
VIDEO_EXTENSIONS = (".mp4", ".avi", ".mov", ".mkv", ".webm")

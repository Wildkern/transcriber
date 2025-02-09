import os
from config import INPUT_DIR, AUDIO_EXTENSIONS, VIDEO_EXTENSIONS

def find_media_files(directory=INPUT_DIR):
    """Recursively finds all media files in a given directory."""
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(AUDIO_EXTENSIONS + VIDEO_EXTENSIONS):
                media_files.append(os.path.join(root, file))
    return media_files

if __name__ == "__main__":
    print(find_media_files())  

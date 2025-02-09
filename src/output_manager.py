import os
import json
from config import OUTPUT_DIR

def save_transcription(original_file, transcription):
    """Saves transcription as JSON and text files."""
    base_name = os.path.basename(original_file).rsplit(".", 1)[0]

    json_path = os.path.join(OUTPUT_DIR, base_name + ".json")
    text_path = os.path.join(OUTPUT_DIR, base_name + ".txt")

    # Save as JSON
    with open(json_path, "w") as json_file:
        json.dump({"file": original_file, "transcription": transcription}, json_file, indent=4)

    # Save as text
    with open(text_path, "w") as text_file:
        text_file.write(transcription)

    print(f"Transcriptions saved: {json_path}, {text_path}")

if __name__ == "__main__":
    save_transcription("sample.mp3", "This is a test transcription.")

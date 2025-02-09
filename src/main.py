from file_parser import find_media_files
from transcriber import transcribe_audio
from output_manager import save_transcription

def main():
    """Main function to process media files for transcription."""
    media_files = find_media_files()
    
    if not media_files:
        print("No media files found in the directory!")
        return

    print(f"Found {len(media_files)} media files. Processing...")

    for file in media_files:
        print(f"Processing: {file}")
        transcription = transcribe_audio(file)
        if transcription:
            save_transcription(file, transcription)

    print("All files processed. Transcriptions saved.")

if __name__ == "__main__":
    main()

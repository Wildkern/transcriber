import os
import whisper
from pydub import AudioSegment
from config import WHISPER_MODEL, AUDIO_EXTENSIONS, VIDEO_EXTENSIONS


model = whisper.load_model(WHISPER_MODEL)

def convert_to_wav(file_path):
    """Converts audio/video files to WAV format for Whisper processing."""
    wav_path = file_path.rsplit(".", 1)[0] + ".wav"

    if file_path.lower().endswith(AUDIO_EXTENSIONS):
        audio = AudioSegment.from_file(file_path)
        audio.export(wav_path, format="wav")

    elif file_path.lower().endswith(VIDEO_EXTENSIONS):
        os.system(f'ffmpeg -i "{file_path}" -ac 1 -ar 16000 "{wav_path}" -y')

    return wav_path

def transcribe_audio(file_path):
    """Transcribes an audio file using Whisper."""
    wav_file = convert_to_wav(file_path)
    try:
        result = model.transcribe(wav_file)
        return result["text"]
    except Exception as e:
        print(f"Error transcribing {file_path}: {e}")
        return None
    finally:
        if os.path.exists(wav_file):
            os.remove(wav_file)  # remove temporary WAV file

if __name__ == "__main__":
    test_file = "test.mp3"  # replace with an actual file
    print(transcribe_audio(test_file))

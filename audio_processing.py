import os
from pydub import AudioSegment
from config import RAW_AUDIO_DIR, WAV_AUDIO_DIR, SAMPLE_RATE, CHANNELS

def normalize_audio():
    os.makedirs(WAV_AUDIO_DIR, exist_ok=True)

    for file in os.listdir(RAW_AUDIO_DIR):
        if not file.endswith(".wav"):
            continue

        audio = AudioSegment.from_wav(os.path.join(RAW_AUDIO_DIR, file))
        audio = audio.set_frame_rate(SAMPLE_RATE).set_channels(CHANNELS)
        audio.export(os.path.join(WAV_AUDIO_DIR, file), format="wav")

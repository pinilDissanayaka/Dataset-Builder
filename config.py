SAMPLE_RATE = 22050
CHANNELS = 1
CHUNK_DURATION_MS = 8000  # 8 seconds
LANGUAGE = "si"

RAW_AUDIO_DIR = "data/raw_audio"
WAV_AUDIO_DIR = "data/wav_audio"
CHUNKS_WAV_DIR = "data/chunks/wavs"
CHUNKS_TEXT_DIR = "data/chunks/text"
FINAL_WAVS_DIR = "data/final_dataset/wavs"
METADATA_PATH = "data/final_dataset/metadata.csv"

WHISPER_MODEL = "large-v3"
DEVICE = "cuda"  # change to "cpu" if no GPU

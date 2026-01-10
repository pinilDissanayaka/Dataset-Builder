from downloader import download_podcast
from audio_processing import normalize_audio
from transcriber import transcribe_audio
from chunker import chunk_with_timestamps
from dataset_builder import build_dataset

if __name__ == "__main__":
    # Sinhala Podcast YouTube URL or Playlist
    YT_URL = "https://www.youtube.com/playlist?list=PLAYLIST_ID"

    download_podcast(YT_URL)
    normalize_audio()

    transcripts = transcribe_audio()
    chunk_data = chunk_with_timestamps(transcripts)

    build_dataset(chunk_data)

    print("✅ Sinhala Podcast TTS dataset ready!")

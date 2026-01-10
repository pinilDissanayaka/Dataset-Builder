import os
from faster_whisper import WhisperModel
from config import WAV_AUDIO_DIR, LANGUAGE, WHISPER_MODEL, DEVICE

def transcribe_audio():
    model = WhisperModel(
        WHISPER_MODEL,
        device=DEVICE,
        compute_type="float16" if DEVICE == "cuda" else "int8"
    )

    results = {}

    for file in os.listdir(WAV_AUDIO_DIR):
        if not file.endswith(".wav"):
            continue

        segments, _ = model.transcribe(
            os.path.join(WAV_AUDIO_DIR, file),
            language=LANGUAGE,
            beam_size=5
        )

        results[file] = [
            {
                "start": seg.start,
                "end": seg.end,
                "text": seg.text.strip()
            }
            for seg in segments
            if seg.text.strip()
        ]

    return results

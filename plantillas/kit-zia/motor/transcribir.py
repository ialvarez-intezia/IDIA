# Tiempos por palabra de la voz (faster-whisper). Uso, desde la carpeta del proyecto:
#   ~/.zia-videos-venv/bin/python <skill>/motor/transcribir.py voz/zia-voz-limpia.wav   -> audio/palabras-whisper.json
#   (con un segundo argumento, p. ej. 18.5, revisa desde ese segundo con el modelo medium)
# La primera vez descarga el modelo "small" (~500 MB).
import json, sys, os, subprocess
import numpy as np
from faster_whisper import WhisperModel
def load(p):  # decodifica con ffmpeg: evita el choque de versiones de PyAV (metadata_errors)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768
src = sys.argv[1]; desde = float(sys.argv[2]) if len(sys.argv) > 2 else None
os.makedirs("audio", exist_ok=True)
if desde is not None:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(desde), "-i", src, "-ac", "1", "-ar", "16000", "audio/_cola.wav"], check=True)
    m = WhisperModel("medium", compute_type="int8")
    for s in m.transcribe(load("audio/_cola.wav"), language="es", word_timestamps=True, beam_size=5)[0]:
        print(s.text); print([(w.word.strip(), round(w.start + desde, 2)) for w in s.words])
    os.remove("audio/_cola.wav"); sys.exit()
m = WhisperModel("small", compute_type="int8")
segs, _ = m.transcribe(load(src), language="es", word_timestamps=True)
words = []
for s in segs:
    print(f"[{s.start:5.2f}-{s.end:5.2f}] {s.text}")
    words += [dict(w=w.word.strip(), s=round(w.start, 2), e=round(w.end, 2)) for w in s.words]
json.dump(words, open("audio/palabras-whisper.json", "w"), ensure_ascii=False, indent=1)
print(" ".join(f"{x['w']}@{x['s']}" for x in words))

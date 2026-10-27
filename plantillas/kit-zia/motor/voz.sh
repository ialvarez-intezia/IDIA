#!/bin/zsh
# Voz de Zia (gratis, Google). Uso, desde la carpeta del proyecto:
#   zsh <skill>/motor/voz.sh "Texto completo que dice Zia."
# Deja voz/zia-voz-original.mp3 y voz/zia-voz-limpia.wav (tono +1,3 semitonos y 12% mas rapida: suena a personaje).
set -e
VENV="$HOME/.zia-videos-venv"
[ -x "$VENV/bin/gtts-cli" ] || { python3 -m venv "$VENV" && "$VENV/bin/pip" -q install gTTS faster-whisper numpy; }
mkdir -p voz
"$VENV/bin/gtts-cli" -l es --tld com.mx "$1" -o voz/zia-voz-original.mp3
ffmpeg -v error -y -i voz/zia-voz-original.mp3 -af "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,asetrate=24000*1.08,aresample=48000,atempo=1.12,highpass=f=90,acompressor=threshold=-24dB:ratio=3:attack=4:release=120:makeup=3,alimiter=limit=0.5:level=false" -ar 48000 -ac 1 voz/zia-voz-limpia.wav
ffprobe -v error -show_entries format=duration -of csv=p=0 voz/zia-voz-limpia.wav | xargs printf "Duracion de la voz: %s s\n"

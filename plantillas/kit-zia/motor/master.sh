#!/bin/zsh
# Master final: mezcla mono -> estereo -> -14 LUFS / -1 dBTP. Uso: ./master.sh  (desde audio/)
set -e
cd "$(dirname "$0")"
ffmpeg -v error -y -i mezcla-pre.wav -af "pan=stereo|c0=c0|c1=c0" -c:a pcm_s24le _st.wav
II=$(ffmpeg -hide_banner -i _st.wav -af loudnorm=I=-14:TP=-1:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p' | python3 -c "import json,sys;print(json.load(sys.stdin)['input_i'])")
G=$(python3 -c "print(-14-($II))")
ffmpeg -v error -y -i _st.wav -af "volume=${G}dB,alimiter=limit=0.84:attack=1:release=40:level=false" -ar 48000 -c:a pcm_s24le mezcla-master.wav
rm _st.wav
for d in ../proyecto-9x16; do [ -d $d ] && cp mezcla-master.wav $d/assets/audio/mezcla.wav; done
ffmpeg -hide_banner -i mezcla-master.wav -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak):"

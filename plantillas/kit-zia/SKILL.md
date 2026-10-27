---
name: zia-videos
description: Hace videos animados con Zía, el personaje de Intezia (el triángulo de la A del logo), con voz, música y efectos hechos en código y la firma de Zía entrando al logo al final. Entrega un MP4 vertical 9:16 listo para mandar. Úsala SIEMPRE que pidan "un video de Zía", "pon a Zía a decir…", "que Zía salude / felicite / anuncie / explique…", "un reel animado con Zía", "un video para el equipo con Zía", aunque no digan la palabra skill. No es para editar videos grabados con cámara ni para presentaciones.
---

# Videos de Zía (Intezia)

Zía es el triángulo amarillo-naranja que vive dentro de la A del logo de Intezia. Sale, hace la vaina y vuelve a meterse en la A con un giro: ese es el cierre de todos sus videos. Este kit trae todo para hacer un video nuevo en ~15 minutos sin gastar créditos de nada.

## 0. Antes de empezar (solo la primera vez)
Revisa que la computadora tenga lo necesario e instala lo que falte (en Mac, con Homebrew):
- `node -v` → Node 18 o más (`brew install node`).
- `ffmpeg -version` (`brew install ffmpeg`).
- `python3 --version` → 3.9 o más.
- La voz y los tiempos se instalan solos en `~/.zia-videos-venv` la primera vez que corres `motor/voz.sh`.
- La primera vez, `npx hyperframes@0.8.106` baja su navegador para renderizar. Tarda un par de minutos.
Haz una prueba renderizando `plantilla/` tal cual (ver paso 7) antes del primer video real.

## 1. Entiende el pedido (máximo una pregunta)
Necesitas: **quién lo va a ver** (interno o redes públicas), **qué dice Zía** (o la idea), **duración** (por defecto ≤ 20 s), **tono**. Si falta algo, pon un default razonable y dilo. Si te dan una idea y no un guion, escribe el guion tú y muéstralo en una línea antes de seguir.

## 2. Reglas de marca (no negociables)
- **Dónde va Zía:** videos animados de Intezia e Instagram de Intezia. **Nunca** en propuestas, decks, correos, la web, el IA TechDay (su personaje es Keia) ni nada de R23 / Club Fénix. Nunca en lugar del logo.
- **Si va a redes públicas, pásalo por Jean (Marketing) antes de publicar.** Lo interno (grupos del equipo) no necesita aprobación.
- **Voz:** el manual dice que Zía no habla y que la voz es de un narrador. En videos **internos** Jean aprobó que hable con voz de mujer (13-oct-2026). En redes públicas, usa narrador (o pregunta).
- **Cuerpo:** usa SIEMPRE `assets/zia.js`. Nunca dibujes a Zía a mano ni le pongas accesorios (lentes, corbatín, sombrero): se parecería al personaje de ChatGPT.
- **Color:** sobre negro o crema va con su degradado (`v: "D"`). Sobre el amarillo Intezia (#FFD300) va la versión negra (`v: "N"`). Nunca degradado sobre amarillo, ni negra sobre negro, ni fondos azul/morado/verde.
- **Paleta:** negro #0A0A0A, amarillo #FFD300, acento #F7941D, claro #FFF27E. Verde solo en un ✓. Tipografía Poppins (títulos) e Instrument Serif itálica (frases con alma).
- **Mensaje de Intezia:** "instalar IA / instalar capacidades", nunca "capacitar", "formar", "curso" ni "taller". Cifras válidas: "+200 empresas". OpenAI: "Grupo Intezia, una de las primeras empresas de Latinoamérica en ser OpenAI Select Partner", y **jamás** nada que ubique ese logro en Venezuela.
- **Logos:** el de Intezia es la imagen (`assets/intezia-white*.png`), nunca escrito en texto. Logos de terceros, solo de Simple Icons en blanco.
- Español venezolano, nada de voseo.

## 3. Arma el proyecto
```
<Nombre del video>/
  voz/            (la voz)
  audio/          (gen_audio.py, master.sh, palabras-whisper.json)
  proyecto-9x16/  (copia de plantilla/)
  final/          (el MP4)
```
Copia `plantilla/` a `proyecto-9x16/` y `motor/gen_audio.py` + `motor/master.sh` a `audio/`.

## 4. Voz y tiempos
```bash
zsh <skill>/motor/voz.sh "¡Hola, equipo! Soy Zía…"
~/.zia-videos-venv/bin/python <skill>/motor/transcribir.py voz/zia-voz-limpia.wav
```
La transcripción da el segundo exacto de cada palabra. **La animación se ajusta a la voz:** cada palabra clave entra en su segundo (súmale el `VO_OFF` de 0,4 s). A ritmo normal salen ~2,8 palabras por segundo: 45 palabras ≈ 16 s de voz + 3,6 s de firma.

## 5. La animación (`proyecto-9x16/index.html`)
La plantilla es un video completo que funciona. Mira también los tres ejemplos de `ejemplos/`. **Reescribe las escenas** para el guion nuevo; no repitas las mismas animaciones de un video a otro (salvo la firma, que es fija).
- Cada escena es un `<div class="clip" data-start data-duration data-track-index>`. Todo lo anima una sola línea de tiempo GSAP (`tl`) en pausa.
- **Zía:** un `<div id="zX" class="zia">` por aparición. Se posiciona con `x`/`y` (la base de Zía, centrada) y `scale`. Fuera de cuadro = `y: 2450` (más arriba se asoma la punta).
- Expresiones: `eyes("#zX", "happy" | "normal" | "surp" | "wink" | "closed" | "worried" | "tired", segundo)`. Cambian de golpe, nunca con fundido.
- Brazos: `armTo("#zX", "L" | "R", grados, duración, segundo)`. El izquierdo sube con grados positivos y el derecho con negativos. Saludar = brazo derecho entre -110 y -140 en vaivén.
- Rebote al aterrizar: `squash(z, segundo, 1.12, 0.86)`. Entra subiendo con `back.out(1.6)` y sale cayendo con `power2.in` en 0,2 s.
- **La firma va al final de todos los videos** (bloque "S8/S7 firma" de la plantilla): el logo aparece con la A vacía, Zía cae encima, saluda, recoge brazos y pies, gira 360° y se convierte en el triángulo de la A. No muevas el logo (`left 230, top 820, width 620`) o tendrás que recalcular `TX/TY/TS`.

**Trampas que ya rompieron videos:**
- Texto con degradado: pon la clase `gradp` en el contenedor; el degradado se aplica a cada palabra `.w`. Si se lo pones al padre de spans animados, el texto desaparece.
- No uses `top`, `name` ni `status` como nombre de variable en el script: chocan con `window` y el video sale en negro sin error visible.
- No pongas `transform` en el CSS de algo que anima GSAP; usa `fromTo` con el estado inicial. Anima `x/y`, no `left/top`.
- Un segundo `fromTo` sobre el mismo elemento lleva `immediateRender: false`.
- Los elementos que se crean por script deben existir antes de animarlos.
- Las palabras de la frase deben caber en 1080 px de ancho: prueba con la toma (paso 6).

## 6. Revisa antes de renderizar
```bash
cd proyecto-9x16
npx --yes hyperframes@0.8.106 check
npx --yes hyperframes@0.8.106 snapshot --at 1.5,4,7,10 -o snaps --no-end
```
Mira `snaps/contact-sheet.jpg`: textos completos y legibles, Zía entera (sin cortes), nada encimado, ningún cuadro vacío. Si todo sale negro, hay un error de JavaScript. `text_not_painted` sobre textos con degradado es un falso positivo.

## 7. Audio y render
```bash
cd audio && python3 gen_audio.py && zsh master.sh && cd ..
cd proyecto-9x16 && npx --yes hyperframes@0.8.106 render --fps 60 --quality delivery --quiet -o ../final/<tema>-9x16-<fecha>.mp4
```
En `gen_audio.py` cambia `DUR`, `END` (cuando arranca la firma) y la lista `C` de efectos: un whoosh cuando algo entra o sale, un pop en cada elemento, un boing cuando Zía aterriza y el "plin" de la firma. Debe imprimir una diferencia voz/música de 15 a 18 dB; si es menor, baja `MG`. `master.sh` deja el audio a -14 LUFS en estéreo.

## 8. Entrega
- Arma una hoja de contacto del video final y revísala: `ffmpeg -i final/X.mp4 -vf "select='isnan(prev_selected_t)+gte(t-prev_selected_t\,1.5)',scale=300:-1,tile=6x2" -frames:v 1 final/hoja.jpg`.
- Manda el MP4 y di en dos líneas qué dice y qué pasa en cada escena.
- Nombre del archivo: tema primero, fecha al final (`zia-saludo-ventas-9x16-2026-10-20.mp4`).

# Video del dashboard — kit de Zía

> Segundo entregable de todo Dashboard de Impacto (desde 2026-10-26): un video vertical corto que
> cuenta el resultado, hecho con el kit de Zía (`plantillas/kit-zia/`). Diseño del dashboard:
> `plantillas/dashboard-edutrace.md`. Mecánica del PDF: `plantillas/generar-dashboard.md`. Flujo
> general: `CLAUDE.md §11`.

---

## 0. Qué es y qué no es

- **Qué es:** un MP4 9:16 a 60 fps de 15 a 25 s (por defecto ≤ 20 s), **aparte del PDF**, que cuenta
  en lenguaje sencillo las 3 o 4 cifras que más pesan del dashboard.
- **Qué no es:** no reemplaza al PDF ni lo repite slide por slide, y no es una pieza de la serie
  semanal de Instagram.
- **El kit:** `plantillas/kit-zia/` es la copia de la skill `zia-videos` (6 MB: motor de voz, tiempos
  y audio, plantilla de HyperFrames, 3 ejemplos y el Manual de uso de Zía v1.1 en
  `manual/zia-manual-de-uso.pdf`). Instrucciones del kit: `plantillas/kit-zia/SKILL.md`, donde
  `<skill>` = `plantillas/kit-zia`.
- **Origen:** el usuario indicó la carpeta de Drive «Kit de Zía para directores»
  (`drive.google.com/drive/folders/1vQFYoGdDf40qMcqO4gyArPRW49bNKIeP`, propietario Jean). Su contenido
  no pudo revisarse el 2026-10-26 (el conector la devolvió vacía); la copia del repo sale de la skill
  instalada. Si el kit cambia en Drive, hay que actualizar la copia.

---

## 1. Reglas de marca — bloqueantes

Salen del Manual de uso de Zía (§02, §09, §11) y de `plantillas/kit-zia/SKILL.md §2`.

1. **Zía solo vive en el video.** Nunca dentro del PDF del dashboard, ni en propuestas, decks,
   cotizaciones, correos o documentos. Las 7 slides del dashboard no llevan a Zía ni su firma.
2. **Aprobación de Jean para el cliente.** El manual limita a Zía a videos animados e Instagram y
   exige la aprobación de Jean para cualquier otro uso. Entregar el video a un cliente se anota como
   uso nuevo: **antes del primer envío se confirma con Jean y se registra aquí la fecha**
   (pendiente al 2026-10-26).
3. **Voz de narrador, no de Zía.** Zía no habla. La voz de mujer de `voz.sh` solo está aprobada para
   videos internos (Jean, 13-oct-2026). Para el cliente, una persona graba el guion (Jean o quien él
   designe) y el audio se guarda como `voz/zia-voz-limpia.wav`, el nombre que lee `gen_audio.py`;
   el resto del flujo es igual.
4. **Mensaje de Intezia:** el video dice «instalar IA» o «instalar capacidades»; **nunca**
   «capacitar», «formar», «curso» ni «taller». El PDF sí puede decir «formación». Sin voseo.
5. **Cifras solo del dashboard y con su naturaleza (§4.17):** «respondió bien el 84%» (medido),
   «declaran ahorrar 2.5 horas por semana» (declarado), «sienten que pueden repetirlo sin ayuda»
   (percibido). Nunca «mejoró» sobre datos declarados o percibidos. Las cifras de la empresa
   («+200 empresas») y la mención de OpenAI, solo con la redacción oficial del kit (`SKILL.md §2`).
6. **Privacidad (§4.16):** ni nombres de participantes, ni cédula, ni correo, ni testimonios sin
   autorización. El nombre del cliente solo si el dashboard ya lo lleva y el cliente autorizó
   mostrarlo. Ojo: `voz.sh` genera la voz con gTTS, que envía el texto del guion a Google; un guion
   de cliente solo lleva cifras agregadas.
7. **Sin acuerdos económicos ni valores (§4.15).** El logo de Intezia es la imagen del kit, nunca
   texto; logos de terceros, solo de Simple Icons en blanco.
8. **Marca visual del video:** la paleta y las fuentes del kit (negro #0A0A0A, amarillo #FFD300,
   acento #F7941D, claro #FFF27E; Poppins e Instrument Serif itálica). Difieren de las del deck
   (§4.1): no se mezclan en una misma pieza. Zía nunca tapa texto, cifras ni logos.

---

## 2. Guion

Estructura del manual (§10): el dolor, la IA lo resuelve, el resultado y la firma en la A. Aplicada
al dashboard:

| Escena | Qué cuenta | Sale de la slide |
|---|---|---|
| 1 · El antes | La tarea con mayor ahorro y cuánto tardaba (declarado) | 03 |
| 2 · Lo que cambió | % que ya aplica lo aprendido y horas por semana (mediana, declarado) | 02 y 03 |
| 3 · Lo que quedó | % de aciertos (medido) o el progreso del grupo (percibido); una sola si no cabe | 04 y 05 |
| 4 · Lo que sigue | El primer paso de la recomendación de Intezia | 07 |
| Firma | Zía entra a la A (fija, ~3,6 s) | |

- **Largo:** unas 45 palabras ≈ 16 s de voz + 3,6 s de firma ≈ 20 s (ritmo de ~2,8 palabras por segundo).
- **Cifras:** 3 o 4 como máximo, y cada una dice de qué es. Ninguna cifra que no esté en el PDF.
- **Guion primero:** se muestra al usuario y se aprueba antes de animar (manual §11).
- **Zía actúa, no habla:** cansada o preocupada en el antes, lanza las tarjetas en la solución,
  celebra en el resultado y nunca termina triste ni derrotada.

---

## 3. Flujo

**Prerrequisitos** (`SKILL.md §0`): Node 18 o más, `ffmpeg`, Python 3.9 o más. La primera vez se
instala `~/.zia-videos-venv` y `npx hyperframes@0.8.106` descarga su navegador (unos minutos).
Revisado el 2026-10-26 en la Mac de trabajo: Node v26, ffmpeg y Python 3.9.6 presentes.

1. **Dashboard terminado:** PDF verificado y revisado (`CLAUDE.md §10` y §11). El video se hace
   después, con las mismas cifras.
2. **Guion** de unas 45 palabras (§2) → aprobado por el usuario.
3. **Carpeta** `clientes/dashboards/<slug>/video/` con `voz/`, `audio/`, `proyecto-9x16/` y `final/`.
4. **Producir con el kit**, `SKILL.md §3 a §8`: copiar `plantilla/` a `proyecto-9x16/` y
   `motor/gen_audio.py` + `motor/master.sh` a `audio/`; voz del narrador (§1.3) → `transcribir.py`
   → escenas en `index.html` (reescribir, sin repetir animaciones de otro video, salvo la firma) →
   `check` y `snapshot` → audio (`DUR`, `END` y la lista `C` de efectos) → `render`.
5. **Revisar la hoja de contacto** del MP4 final: Zía entera, nada tapado, textos legibles y la
   firma encajada en la A (`SKILL.md §8`).
6. **Nombre:** `dashboard-<slug>-9x16-<AAAA-MM-DD>.mp4` en `video/final/` (tema primero, fecha al final).

> **Qué se versiona:** el MP4 final y `proyecto-9x16/` (HTML y assets). No se versionan `voz/` (la
> grabación del narrador), `audio/` ni `proyecto-9x16/snaps/` (ver `.gitignore`).

---

## 4. Checklist pre-entrega del video

- [ ] Zía no aparece en el PDF ni en ningún documento (§1.1).
- [ ] Cada cifra coincide con el PDF y lleva su naturaleza: medido, declarado o percibido (§1.5).
- [ ] Sin nombres de personas, cédula, correo ni testimonios sin autorización (§1.6).
- [ ] Sin «capacitar», «formar», «curso» ni «taller»; sin voseo; sin términos económicos (§1.4, §1.7).
- [ ] Voz de narrador (no la de Zía) y guion aprobado (§1.3, §2).
- [ ] Hoja de contacto revisada cuadro a cuadro (§3.5).
- [ ] Aprobación de Jean registrada para enviar videos a clientes (§1.2).

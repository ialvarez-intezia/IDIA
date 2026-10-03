# Auditoría automática de propuestas por correo

Revisa la bandeja de entrada de `irodriguez@intezia.com`, la cruza con la base de
conocimiento (`clientes/INDEX.json`) y con la hoja **Control de codificación**, y
envía un **reporte priorizado por correo**. Corre **en la nube (GitHub Actions)**,
así que funciona aunque la laptop esté apagada.

Conexión 100% por **CLI / API** (sin MCP).

---

## Qué reporta

1. 🔴 **Solicitudes nuevas** — sin código y sin propuesta (hay que arrancar).
2. 🟠 **Backlog** — código ya asignado en el Sheet pero sin deck construido.
3. 🟢 **Activas** — ya construidas (sin acción de diseño).
4. 🔵 **Posibles cambios de estado** — aprobada / perdida detectados en el correo.
5. 📐 **Próximos códigos libres** por categoría (CU/DIP/TA/CAP/CH).

---

## Piezas

| Archivo | Rol |
|---|---|
| `scripts/google-auth-intezia.py` | Autenticación OAuth (una vez). Genera `token-intezia.json`. |
| `scripts/auditar-correo.py` | El cruce de 3 fuentes + envío del reporte. |
| `.github/workflows/auditoria-correo.yml` | Cron semanal en la nube (lunes 08:00 VET). |
| `scripts/credentials.json` · `scripts/token-intezia.json` | Credenciales. **Gitignored — nunca se versionan.** |

Uso local:
```bash
python3 scripts/auditar-correo.py            # imprime el reporte
python3 scripts/auditar-correo.py --email    # además lo envía por correo
python3 scripts/auditar-correo.py --dias 7   # otra ventana
```

---

## Puesta en marcha — 4 pasos manuales (una sola vez)

> Estos pasos requieren tu cuenta de Google y tu repo de GitHub; el sistema no
> puede hacerlos por ti.

### 1. Re-autorizar con permiso de envío
El token actual es de solo lectura. Para que pueda **enviar** el correo:
```bash
python3 scripts/google-auth-intezia.py
```
Se abre el navegador → inicia sesión como **irodriguez@intezia.com** → acepta el
permiso de envío. Regenera `scripts/token-intezia.json`.

### 2. Publicar el OAuth en «Producción» — CRÍTICO
En [Google Cloud Console](https://console.cloud.google.com/) → proyecto
`idyllic-pact-494602-a6` → **APIs y servicios → Pantalla de consentimiento de OAuth**
→ botón **«Publicar aplicación»** (pasar de *Testing* a *Production*).

> ⚠️ Si se queda en *Testing*, Google **expira el token cada 7 días** y el cron
> semanal dejará de funcionar. En *Production* el token no expira.

### 3. Cargar los Secrets en GitHub
En el repo `Isaac150305/intezia-propuestas` → **Settings → Secrets and variables →
Actions → New repository secret**. Crea dos:

| Secret | Contenido |
|---|---|
| `GOOGLE_CREDENTIALS` | todo el contenido de `scripts/credentials.json` |
| `GOOGLE_TOKEN` | todo el contenido de `scripts/token-intezia.json` (el del paso 1) |

```bash
# Para copiar el contenido al portapapeles (macOS):
cat scripts/credentials.json | pbcopy     # pégalo en GOOGLE_CREDENTIALS
cat scripts/token-intezia.json | pbcopy   # pégalo en GOOGLE_TOKEN
```

### 4. Subir y probar
```bash
git add scripts/auditar-correo.py scripts/google-auth-intezia.py \
        .github/workflows/auditoria-correo.yml scripts/README-auditoria.md .gitignore
git commit -m "feat(auditoria): revisión automática de propuestas por correo"
git push
```
Luego en GitHub → pestaña **Actions → «Auditoría semanal de propuestas» → Run
workflow** para dispararla a mano y verificar que llega el correo.

---

## Notas de mantenimiento

- **Horario:** el cron usa UTC. `0 12 * * 1` = lunes 12:00 UTC = **08:00 VET**.
  Cambia la línea `cron:` en el `.yml` para otra hora/frecuencia
  (`0 12 * * 1-5` = lun-vie).
- **Si re-autorizas** (regeneras el token), vuelve a actualizar el secret
  `GOOGLE_TOKEN` con el nuevo contenido.
- GitHub **desactiva** los cron tras 60 días sin commits en el repo. Como aquí se
  commitea seguido, no aplica; si pasara, basta con reactivarlo en Actions.
- El reporte es solo lectura + envío de correo. **No construye propuestas ni toca
  `meta.json`** (autonomía «solo reporta», respeta §8 de `CLAUDE.md`).

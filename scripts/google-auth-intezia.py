#!/usr/bin/env python3
"""
Autenticación OAuth2 para irodriguez@intezia.com
Corre una sola vez (o cuando el token expire y no pueda renovarse).
Guarda el token en scripts/token-intezia.json para uso de auditar-correo.py

Uso:
    python3 scripts/google-auth-intezia.py
"""

import os
import json
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

BASE_DIR = Path(__file__).parent.parent
CREDENTIALS_FILE = BASE_DIR / "scripts" / "credentials.json"
TOKEN_FILE = BASE_DIR / "scripts" / "token-intezia.json"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",      # para enviarte el reporte por correo
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
]

def autenticar():
    if not CREDENTIALS_FILE.exists():
        print(f"ERROR: No se encontró {CREDENTIALS_FILE}")
        print("Descarga el credentials.json de Google Cloud Console y colócalo en scripts/")
        return None

    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Token expirado — renovando automáticamente...")
            creds.refresh(Request())
        else:
            print("Abriendo navegador para autenticar irodriguez@intezia.com ...")
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE),
                SCOPES,
            )
            # login_hint sugiere la cuenta correcta en el selector de Google
            creds = flow.run_local_server(
                port=0,
                login_hint="irodriguez@intezia.com",
                prompt="consent",
            )

        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
        print(f"Token guardado en {TOKEN_FILE}")

    # Verificar cuenta autenticada
    import urllib.request
    try:
        req = urllib.request.Request(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers={"Authorization": f"Bearer {creds.token}"},
        )
        with urllib.request.urlopen(req) as resp:
            info = json.loads(resp.read())
            print(f"\nAutenticado como: {info.get('email')}")
            if info.get("email") != "irodriguez@intezia.com":
                print("ADVERTENCIA: la cuenta autenticada no es irodriguez@intezia.com")
                print("Borra scripts/token-intezia.json y vuelve a correr este script.")
    except Exception as e:
        print(f"No se pudo verificar la cuenta: {e}")

    return creds


if __name__ == "__main__":
    autenticar()
    print("\nListo. Ahora puedes correr: python3 scripts/auditar-correo.py")

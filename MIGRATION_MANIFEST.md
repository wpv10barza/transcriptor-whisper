# Migration Manifest — Transcriptor Whisper

- source: Google Drive
- source_folder: `Codigos_Antes_Exportados/Transcriptor`
- project_family: `Transcriptor / Whisper`
- version: snapshot auditado 2026-09-29
- github_repository: `wpv10barza/transcriptor-whisper`
- github_branch: `import/drive-2026-09-29`
- github_commit: pendiente hasta verificación final
- verification_status: `PENDING_GITHUB_CI`
- verified_at: pendiente

## Archivos migrados

- `run_whisper.py` — lógica de transcripción; la ruta fija local del audio fue sustituida por argumento/variable `TRANSCRIPTOR_AUDIO`.
- `requirements.txt` — dependencias originales.
- `setup_windows.ps1` — setup original.
- `docs/README_WINDOWS.md` — guía Windows derivada del archivo original.

## Archivos preservados solo en Drive

Los siguientes archivos contienen una transcripción de entrevista incrustada y no se publican en el repositorio público:

| Archivo | SHA-256 | Motivo |
|---|---|---|
| `Transcriptor.py` | `a483d770d8ba6fff5f9ec6936ef0ef44d8cbb5f5d615e3f08c363468061de75a` | exportación Colab con entrevista embebida |
| `Transcriptor.ipynb` | `ed8f02d95864063be6fc95d057e1f42d1579300293d261c2519f37dfa8981c8d` | notebook con entrevista embebida |

## SHA-256 de archivos de origen migrados

- `run_whisper.py`: `deec64156267bf2b8f68c2993a44e6ba56d9b2601a5a612da4b0c2d45eddc268`
- `requirements.txt`: `77d1516c8483bfcd757fe7359d0a0464ba278890f07b41f0269e42d2aa5efd85`
- `README_WINDOWS.md`: `0fdb3026732411df14c0044ccd578d6d99ff0ab2d9935a6088e7e3f2cf9b1743`
- `setup_windows.ps1`: `d63c28db99de72b1dc3ae520e09936e7972ba9aae5823dd4d6c4810e4e1630d9`

## Proyecto `Transcripción`

Auditado por separado. Su servicio FastAPI/Gradio/Whisper/Gemma no comparte estructura demostrable con `Transcriptor`; la subcarpeta `whisplay-ai-chatbot` corresponde a un proyecto externo de PiSugar. No se fusiona automáticamente y permanece en Drive.

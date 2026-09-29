# Transcriptor Whisper

Repositorio canónico reconstruido desde el proyecto `Transcriptor` de Google Drive.

## Propósito observado
Transcribir archivos de audio con OpenAI Whisper y preparar resultados para análisis posterior. El proyecto original incluye una ejecución en Windows, un notebook de Colab y una exportación de ese notebook.

## Tecnologías observadas
- Python
- OpenAI Whisper
- PyTorch
- FFmpeg
- pandas y tqdm en el flujo histórico de análisis

## Estructura canónica
- `run_whisper.py`: transcripción local con Whisper.
- `requirements.txt`: dependencias registradas en el proyecto original.
- `docs/README_WINDOWS.md`: instrucciones originales para Windows.
- `setup_windows.ps1`: preparación original del entorno Windows.
- `MIGRATION_MANIFEST.md`: inventario, hashes y exclusiones.

## Privacidad y preservación
`Transcriptor.ipynb` y `Transcriptor.py` se conservan en Google Drive y no se publican aquí porque contienen una transcripción de entrevista incrustada. Sus hashes se registran en el manifest para poder demostrar identidad sin exponer el contenido.

## Proyecto relacionado no fusionado
La carpeta `Transcripción` fue auditada por separado. Su arquitectura FastAPI/Gradio/Whisper/Gemma y la copia externa `whisplay-ai-chatbot` no demuestran una genealogía de código con este proyecto, por lo que no se fusionan automáticamente.

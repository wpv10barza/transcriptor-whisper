import argparse
import os
import torch
import whisper


def inicializar_y_transcribir(audio_path: str, model_name: str = "base") -> int:
    print("\n=======================================================")
    print("🚀 INICIANDO PIPELINE DE TRANSCRIPCIÓN SIMBIÓTICA")
    print("=======================================================")

    if not os.path.exists(audio_path):
        print(f"❌ ERROR: El archivo de audio no existe en: {audio_path}")
        return 1

    print("✔ Audio detectado correctamente.")
    print(f"📦 Cargando PyTorch ({torch.__version__}) compartido...")

    try:
        print(f"🧠 Cargando modelo '{model_name}' en la CPU...")
        model = whisper.load_model(model_name, device="cpu")
        print("🎙 Transcribiendo audio...")
        resultado = model.transcribe(audio_path, language="es")

        print("\n📝 --- TRANSCRIPCIÓN COMPLETADA ---")
        print(resultado["text"].strip())
        print("=======================================================\n")
        return 0
    except Exception as exc:
        print(f"\n❌ CRITICAL ERROR: {exc}")
        print("💡 TIP DEVOPS: Los archivos .opus requieren FFmpeg instalado.")
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribir audio local con OpenAI Whisper")
    parser.add_argument("audio", nargs="?", default=os.environ.get("TRANSCRIPTOR_AUDIO"), help="Ruta del archivo de audio")
    parser.add_argument("--model", default=os.environ.get("WHISPER_MODEL", "base"), help="Modelo Whisper")
    args = parser.parse_args()

    if not args.audio:
        parser.error("indica una ruta de audio o define TRANSCRIPTOR_AUDIO")
    return inicializar_y_transcribir(args.audio, args.model)


if __name__ == "__main__":
    raise SystemExit(main())

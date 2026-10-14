
import argparse
import subprocess
import sys
from pathlib import Path

MODEL_PATH = Path("./model/vaani-multi.gguf")
PARAKEET_CLI = Path("./runtime/parakeet-cli")


def transcribe_audio(audio_path: Path) -> str:
    """Transcribe an audio file and return the transcript."""

    if not audio_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if not MODEL_PATH.is_file():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH.resolve()}"
        )

    if not PARAKEET_CLI.is_file():
        raise FileNotFoundError(
            f"Parakeet CLI not found: {PARAKEET_CLI.resolve()}"
        )

    command = [
        str(PARAKEET_CLI.resolve()),
        "transcribe",
        "--model",
        str(MODEL_PATH.resolve()),
        "--input",
        str(audio_path.resolve()),
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        error = result.stderr.strip() or "Transcription failed."
        raise RuntimeError(error)

    # Prefer stdout; use stderr if the CLI prints its output there.
    transcript = result.stdout.strip()

    if not transcript:
        transcript = result.stderr.strip()

    return transcript


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file using the Vaani model."
    )

    parser.add_argument(
        "audio",
        type=Path,
        help="Path to the input WAV audio file",
    )

    args = parser.parse_args()

    try:
        transcript = transcribe_audio(args.audio)
        print(transcript)

    except (FileNotFoundError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

# Vaani Audio Transcription

A simple Python script to transcribe audio files using the Vaani model and `parakeet-cli`.

## Project Structure

```text
your-project/
├── transcribe.py
├── model/
│   └── vaani-multi.gguf
└── runtime/
    └── parakeet-cli
```

## 1. Prerequisites

- Python 3.10 or later
- Vaani GGUF model
- Compiled `parakeet-cli` executable

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the virtual environment.

**Linux / macOS:**

```bash
source .venv/bin/activate
```

## 3. Run Transcription

Pass the audio file path as an argument.

```bash
python transcribe.py ./audio/kannada.wav
```

The script prints the transcription to the terminal.

## 5. Deactivate the Virtual Environment

When you finish, run:

```bash
deactivate
```

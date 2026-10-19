# Deterministic Parser Training Dataset Synthesizer

Evidence-driven generation and validation pipeline for deterministic CLI command datasets.

## Current capabilities

- CLI evidence loading
- Constraint extraction
- Candidate generation
- Deterministic validation pipeline
- Configurable LLM provider abstraction
- Mock LLM backend for testing

## Requirements

- Ubuntu 24.04
- Python 3.11+
- uv

## Setup

```bash
git clone https://github.com/foaly717/Deterministic-Parser-Training-Dataset-Synthesizer.git
cd Deterministic-Parser-Training-Dataset-Synthesizer
uv sync
```

## Test

```bash
uv run pytest
```

## Runtime configuration

Runtime behavior can be configured with environment variables:

```bash
MODEL_PROVIDER=openai_compatible
MODEL_NAME=default
MODEL_ENDPOINT=http://127.0.0.1:8080/v1/chat/completions
HELP_FILE=data/evidence/handbrakecli-help.txt
OUTPUT_FILE=data/raw/livefire_20.jsonl
```

Configuration priority:

```
CLI argument
    >
environment variable
    >
default value
```

## Live generation

OpenAI-compatible provider:

```bash
uv run python scripts/live_generate_20.py \\
  --provider openai_compatible \\
  --endpoint http://127.0.0.1:8080/v1/chat/completions \\
  --model default \\
  --help-file data/evidence/ffmpeg-help.txt \\
  --count 5
```

Mock provider:

```bash
uv run python scripts/live_generate_20.py \\
  --provider mock \\
  --help-file data/evidence/ffmpeg-help.txt \\
  --count 5
```

The mock provider allows generator and validator testing without a running model server.

## Repository contents

Tracked:

- source code
- tests
- evidence fixtures
- normalized datasets
- dependency lock files

Not tracked:

- virtual environments
- generated outputs
- local model files (*.gguf)

Large model files should be managed separately from git.

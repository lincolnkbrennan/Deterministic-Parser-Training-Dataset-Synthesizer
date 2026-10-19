import subprocess
from pathlib import Path


def test_dataset_diversity_runs():
    fixture = Path("tests/fixtures/sample_livefire.jsonl")

    result = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "scripts/dataset_diversity.py",
            "--input",
            str(fixture),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "DATASET DIVERSITY REPORT" in result.stdout

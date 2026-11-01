"""Check every Python solution against answers.txt and the one-minute rule."""

import importlib.util
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS = sorted((ROOT / "python").glob("p[0-9][0-9][0-9].py"))
TIME_LIMIT = 60  # seconds: Project Euler's one-minute rule


def load_answers() -> dict[int, str]:
    answers = {}
    for line in (ROOT / "answers.txt").read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            number, answer = line.split()
            answers[int(number)] = answer
    return answers


ANSWERS = load_answers()


@pytest.mark.parametrize("path", SOLUTIONS, ids=lambda p: p.stem)
def test_solution(path: Path) -> None:
    number = int(path.stem[1:])
    if number not in ANSWERS:
        pytest.skip(f"no answer recorded for problem {number}")

        spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    start = time.perf_counter()
    result = module.solve()
    elapsed = time.perf_counter() - start

    assert str(result) == ANSWERS[number]
    assert elapsed < TIME_LIMIT, f"took {elapsed:.1f}s"
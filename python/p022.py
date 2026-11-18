from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def solve() -> int:
    text = (DATA / "0022_names.txt").read_text().replace('"', '')
    names = text.split(',')
    names.sort()
    total = 0
    position = 1
    print(names)
    for name in names:
        for ch in name:
            total += ((ord(ch) - 64) * position)
        position += 1
    return total

if __name__ == "__main__":
    print(solve())
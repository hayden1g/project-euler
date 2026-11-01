def solve(limit: int = 4000000) -> int:
    first, second = 1, 2
    total = 0
    while second < limit:
        if second % 2 == 0:
            total += second
        first, second = second, second + first
    return total


if __name__ == "__main__":
    print(solve())
def solve(limit: int = 1000) -> int:
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


if __name__ == "__main__":
    print(solve())
def solve(limit: int = 600851475143) -> int:
    largest = 0
    i = 2
    while limit > 1:
        if limit % i == 0:
            limit //= i
            largest = i
        else:
            i += 1
    return largest

if __name__ == "__main__":
    print(solve())
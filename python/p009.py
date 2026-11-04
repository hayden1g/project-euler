def solve(limit: int = 1000) -> int:
    for c in range(limit):
        for b in range(c):
            for a in range(b):
                if a**2 + b**2 == c**2 and a+b+c == limit:
                    return a*b*c
    return 0

if __name__ == "__main__":
    print(solve())
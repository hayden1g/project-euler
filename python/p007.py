import math

def solve(limit: int = 10001) -> int:
    counter = 0
    i = 2
    while True:
        prime = True
        for j in range(2, math.isqrt(i) + 1):
            if i % j == 0:
                prime = False
        if prime:
            counter += 1
        if counter == limit:
            return i
        i += 1

if __name__ == "__main__":
    print(solve())
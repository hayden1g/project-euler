import math

def solve(limit: int = 2000000) -> int:
    sum_primes = 2
    for n in range(3,limit,2):
        prime = True
        for j in range(2, math.isqrt(n) + 1):
            if n % j == 0:
                prime = False
        if prime:
            sum_primes += n
    return sum_primes

if __name__ == "__main__":
    print(solve())
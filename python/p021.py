import math

def divisor_sum(n: int) -> int:
    total = 1
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            total += d
            if d != n // d:
                total += n // d
    return total

def solve(limit: int = 10000) -> int:
    sumOfAllAmicable = 0
    for i in range(1,limit):
        b = divisor_sum(i)
        if b != i and divisor_sum(b) == i:
            sumOfAllAmicable += i
    return sumOfAllAmicable
            

if __name__ == "__main__":
    print(solve())
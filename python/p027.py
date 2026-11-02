import math

def solve() -> int:
    maxcounter = 0
    ans = 0
    for a in range(-999,1000):
        for b in range(-1000,1001):
            n = 0
            primes = True
            counter = 0
            while primes is True:
                current = n*n + a*n + b
                for i in range(2,math.isqrt(abs(current))+1):
                    if current % i == 0 or current < 2:
                        primes = False
                        break
                if primes is True:
                    counter += 1
                n += 1
            if counter > maxcounter:
                maxcounter = counter
                ans = a * b
    return ans

if __name__ == "__main__":
    print(solve())
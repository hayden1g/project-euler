import math

def solve() -> int:
    x = math.factorial(100)
    digitsum = 0
    for digit in str(x):
        digitsum += int(digit)
    return digitsum
            

if __name__ == "__main__":
    print(solve())
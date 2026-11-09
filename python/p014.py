import math

def solve(limit: int = 1000000) -> int:
    maxLength = 0
    for i in range(1,limit):
        chainLength = 0
        num = i
        while num != 1:
            if num % 2 == 0:
                num /= 2
            else:
                num = 3*num + 1
            chainLength += 1
        if chainLength > maxLength:
            maxLength = chainLength
            maxn = i
    return maxn

if __name__ == "__main__":
    print(solve())
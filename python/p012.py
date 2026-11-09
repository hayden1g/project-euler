import math

def solve(limit: int = 500) -> int:
    found = False
    triangleNum = 0
    count = 1
    while not found:
        triangleNum += count
        divisorCount = 0
        for i in range(1, math.isqrt(triangleNum) + 1):
            if triangleNum % i == 0:
                divisorCount += 2
        if divisorCount > 500:
            found = True
        count += 1
    return triangleNum

if __name__ == "__main__":
    print(solve())
import math

def solve(limit: int = 500) -> int:
    triangleNum = 0
    count = 1
    while True:
        triangleNum += count
        divisorCount = 0
        for i in range(1, math.isqrt(triangleNum) + 1):
            if triangleNum % i == 0:
                divisorCount += 2
        if math.isqrt(triangleNum)**2 == triangleNum:
            divisorCount -= 1
        if divisorCount > limit:
            return triangleNum
        count += 1

if __name__ == "__main__":
    print(solve())
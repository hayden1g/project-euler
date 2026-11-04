import math

def solve(limit: int = 2000000) -> int:
    intlist = [True] * limit
    intlist[0] = False
    intlist[1] = False
    count = 0
    for p in range(math.isqrt(limit) + 2):
        if intlist[p]:
            for x in range(p*p, limit, p):
                intlist[x] = False
    for i in range(len(intlist)):
        if intlist[i]:
            count += i
    return count
            

if __name__ == "__main__":
    print(solve())
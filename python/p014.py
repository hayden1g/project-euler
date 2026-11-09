def solve(limit: int = 1000000) -> int:
    maxLength = 0
    lengthdict = {}
    for i in range(1,limit):
        chainLength = 0
        num = i
        while num != 1:
            if num in lengthdict:
                chainLength += lengthdict[num]
                num = 1
            else:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = 3*num + 1
                chainLength += 1
        if chainLength > maxLength:
            maxLength = chainLength
            maxn = i
        lengthdict[i] = chainLength
    return maxn

if __name__ == "__main__":
    print(solve())
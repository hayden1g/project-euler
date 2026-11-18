import math

def solve() -> int:
    divisorsum = 0
    abundantnums = set()
    intlist = [False] * 28124
    for num in range(2,28123):
        divisorsum = 0
        for divisor in range(1, math.isqrt(num)+1):
            if num % divisor == 0:
                divisorsum += num // divisor
                if divisor * divisor != num:
                    divisorsum += divisor
        divisorsum -= num
        if divisorsum > num:
            abundantnums.add(num)
            for n in abundantnums:
                if n+num <= 28123:
                    intlist[n+num] = True
    sumall = 0
    index = 0
    for i in intlist:
        if not i:
            sumall += index
        index += 1
    return sumall

if __name__ == "__main__":
    print(solve())
import math

def solve(limit: int = 10000) -> int:
    sumOfAllAmicable = 0
    for i in range(1,limit):
        divisorsum = 1
        for divisor in range(2,math.isqrt(i)):
            if i % divisor == 0:
                divisorsum += divisor
                divisorsum += i//divisor
        if math.isqrt(i)**2 == i:
            divisorsum += math.isqrt(i)

        testsum = 1
        for divisor in range(2,math.isqrt(divisorsum)):
            if divisorsum % divisor == 0:
                testsum += divisor
                testsum += divisorsum//divisor
        if math.isqrt(i)**2 == i:
            testsum += math.isqrt(divisorsum)
        if testsum == i and divisorsum != i:
            sumOfAllAmicable += i
    return sumOfAllAmicable
            

if __name__ == "__main__":
    print(solve())
def solve() -> int:
    remainders = set()
    foundend = False
    maxdigits = 0
    maxnum = 0
    for i in range(1,1000):
        digits = 1
        remainders = set()
        remainder = 1
        foundend = False
        while foundend is False:
            remainder = remainder*10 % i
            if remainder in remainders:
                foundend = True
            else:
                remainders.add(remainder)
                digits += 1
                
        if digits > maxdigits:
            maxdigits = digits
            maxnum = i
    return maxnum

if __name__ == "__main__":
    print(solve())
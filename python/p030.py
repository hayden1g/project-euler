def solve() -> int:
    # Since 9^5+9^5+9^5+9^5+9^5+9^5 = 354294, no number above that will
    # ever have a sum big enough. 7 digit numbers will always have a sum
    # of 6 digits.
    sumall = 0
    for a in range(2,354294):
        sumdigits = 0
        for digit in str(a):
            sumdigits += int(digit)**5
        if sum == a:
            sumall += sumdigits
    return sumall


if __name__ == "__main__":
    print(solve())
import math

def solve() -> int:
    perms = 1000000
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    finalnum = ""
    for i in range(10):
        num = 9-i
        digit = 0
        while True:
            if perms - math.factorial(num) > 0:
                perms -= math.factorial(num)
                digit += 1
            else:
                break
        finalnum += str(digits[digit])
        digits.remove(digits[digit])
    return int(finalnum)
            

if __name__ == "__main__":
    print(solve())
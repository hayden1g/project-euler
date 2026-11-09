def solve() -> int:
    x = 2**1000
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum
            

if __name__ == "__main__":
    print(solve())
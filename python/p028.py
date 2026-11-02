def solve() -> int:
    num = 1
    sum = 0
    counter = 1
    adder = 0
    while num < 1001*1001:
        num += adder
        if counter % 4 == 1:
            adder += 2
        sum += num
        counter += 1

    return sum

if __name__ == "__main__":
    print(solve())
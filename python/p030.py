def solve() -> int:
    # Since 9^5+9^5+9^5+9^5+9^5+9^5 = 354294, no number above that will
    # ever have a sum big enough.
    all = 0
    for a in range(2,354294):
        sum = 0
        for digit in str(a):
            sum += int(digit)**5
        if sum == a:
            all += sum
    return all


if __name__ == "__main__":
    print(solve())
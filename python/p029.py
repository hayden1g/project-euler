def solve() -> int:
    nums = []
    for a in range(2,101):
        for b in range(2, 101):
            nums.append(a**b)

    return len(set(sorted(nums)))


if __name__ == "__main__":
    print(solve())
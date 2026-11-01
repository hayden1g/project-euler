def solve() -> int:
    # I mainly used math to solve this. Prime factorizations
    # are: 2, 3, 2^2, 5, 3*2, 7, 2^3, 3^2, 5*2, 11, 3^2*2,
    # 13, 7*2, 5*3, 2^4, 17, 3^2*2, 19, 5*2^2. Thus, the
    # answer should be:
    return 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19

if __name__ == "__main__":
    print(solve())
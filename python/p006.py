def solve(limit: int = 100) -> int:
    sum_squares, square_sum = 0, 0
    for i in range(1, limit+1):
        sum_squares += i*i
        square_sum += i
    square_sum **= 2
    return abs(square_sum - sum_squares)

if __name__ == "__main__":
    print(solve())
import math

def solve() -> int:
    # The moves are a combination of 20 across and 20 down.
    # This results in 40!/(20! * 20!) possible ways.
    return int(math.factorial(40) / (math.factorial(20) * math.factorial(20)))

if __name__ == "__main__":
    print(solve())
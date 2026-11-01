def solve() -> int:
    a, b = 100, 100
    largest = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            product = a*b
            if int(str(product)[::-1]) == product and product > largest:
                largest = product
    return largest


if __name__ == "__main__":
    print(solve())
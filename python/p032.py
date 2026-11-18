def solve() -> int:
    products = set()
    digits = [1,2,3,4,5,6,7,8,9]
    # The product must be 2 digit * 3 digit = 5 digit,
    # or 1 * 4 = 5. We can say a must be either 1 or 2
    # digits, and b must be either 3 or 4.
    for a in range(100):
        for b in range(100,10000):
            st = str(a) + str(b) + str(a*b)
            d = []
            if len(st) < 11:
                for num in st:
                    d.append(int(num))
                if sorted(d) == digits:
                    products.add(a*b)
    return sum(products)


if __name__ == "__main__":
    print(solve())
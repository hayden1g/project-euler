def solve() -> int:
    a, b = 1, 1
    index = 3
    while True:
        a, b = a+b, a
        if len(str(a)) == 1000:
            break
        index += 1
    return index
            

if __name__ == "__main__":
    print(solve())
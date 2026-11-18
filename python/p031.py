def solve() -> int:
    coins = [1,2,5,10,20,50,100,200]
    ways = [1] + 200*[0]
    for coin in coins:
        for i in range(coin, 201):
            ways[i] += ways[i-coin]
    return ways[200]


if __name__ == "__main__":
    print(solve())
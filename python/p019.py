def solve() -> int:
    days = 1
    count = 0
    for year in range(1900,2001):
        for month in range(1,13):
            if month in (1, 3, 5, 7, 8, 10, 12):
                days += 31
            elif month in (4, 6, 9, 11):
                days += 30
            else:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    days += 29
                else:
                    days += 28
            if days % 7 == 0 and year > 1900:
                count += 1
    return count
            

if __name__ == "__main__":
    print(solve())
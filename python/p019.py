def solve() -> int:
    days = 0
    count = 0
    for year in range(1900,2001):
        for month in range(1,13):
            if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
                days += 31
            elif month == (4 or 6 or 9 or 11):
                days += 30
            else:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    days += 29
                else:
                    days += 28
            if days % 7 == 0:
                count += 1
    return count
            

if __name__ == "__main__":
    print(solve())
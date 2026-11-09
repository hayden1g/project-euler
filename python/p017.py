units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def solve() -> int:
    words = []
    for i in range(1, 1000):
        if i < 10:
            words.append(units[i])
        elif i < 20:
            words.append(teens[i-10])
        elif i < 100:
            words.append(tens[int(str(i)[0])] + units[int(str(i)[1])])
        else:
            word = units[i // 100] + "hundred"
            x = i % 100
            if x != 0:
                word += "and"
            if x < 10:
                word += (units[x])
            elif x < 20:
                word += (teens[x-10])
            elif x < 100:
                word += (tens[int(str(x)[0])] + units[int(str(x)[1])])
            words.append(word)
    words.append("onethousand")
    letterCount = 0
    for word in words:
        letterCount += len(word)
    return letterCount
            

if __name__ == "__main__":
    print(solve())
string = input()
substring = 'f'

posStart = string.find(substring)
if posStart != -1:
    print(posStart)

posNeg = string[::-1].find(substring)
if posNeg != -1:
    posEnd = len(string) - posNeg - 1
    if posEnd != posStart:
        print(posEnd)

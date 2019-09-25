string = input()
substring = 'h'

posStart = string.find(substring)

posNeg = string[::-1].find(substring)
posEnd = len(string) - posNeg - 1

stringPiece = string[posStart + 1: posEnd]
stringPiece = stringPiece.replace('h', 'H')

if posStart == posEnd:
    posStart = posStart - 1

stringNew = string[:posStart + 1] + stringPiece + string[posEnd:]

print(stringNew)

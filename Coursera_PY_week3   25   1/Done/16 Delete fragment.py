string = input()
substring = 'h'

posStart = string.find(substring)
posNeg = string[::-1].find(substring)
posEnd = len(string) - posNeg - 1

print(string[:posStart], string[posEnd + 1:], sep='')

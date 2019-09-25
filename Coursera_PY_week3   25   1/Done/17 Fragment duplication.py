string = input()
substring = 'h'

if string.find(substring) != -1:
    posStart = string.find(substring)
    posEnd = len(string) - string[::-1].find(substring) - 1
    subStringForDuble = string[posStart + 1:posEnd] * 2
    if posStart == posEnd:
        posEnd += 1
    string = string[:posStart + 1] + subStringForDuble + string[posEnd:]

print(string)

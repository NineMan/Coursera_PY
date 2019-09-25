string = input()
substring = ' '

posSpace = string.find(substring)
print(string[posSpace + 1:], string[:posSpace])

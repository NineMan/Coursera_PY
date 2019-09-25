a = int(input())
b = int(input())

c = 0 ** (a % b)
x = 'YES' * c + 'NO' * (1 - c)
print(x)

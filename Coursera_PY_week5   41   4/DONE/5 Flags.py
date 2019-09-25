n = int(input())

print('+___ ' * n)
for i in range(n):
    string2 = '|' + str(i + 1) + ' / '
    print(string2, end='')
print()
print('|__\\ ' * n)
print('|    ' * n)

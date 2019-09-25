n = int(input())
strings = []
for i in range(n):
    strings.append(input())
print('\n'.join(sorted(strings, key=len)))
numList = list(map(int, input().split()))

finStr = ''
for i in numList:
    if not (i % 2):
        finStr += str(i) + ' '
print(finStr)

numberList = list(map(int, input().split()))
k, c = list(map(int, input().split()))

i = k
while i < len(numberList):
    cTemp = numberList[i]
    numberList[i] = c
    c = cTemp
    i += 1

numberList.append(c)
print(*numberList)

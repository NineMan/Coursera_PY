numberList = list(map(int, input().split()))

for i in range(1, len(numberList), 2):
    tempNumber = numberList[i]
    numberList[i] = numberList[i - 1]
    numberList[i - 1] = tempNumber
print(*numberList)

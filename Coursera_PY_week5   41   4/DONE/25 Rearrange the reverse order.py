numberList = list(map(int, input().split()))

index = 0
length = len(numberList)
while index < length // 2:
    tempNumber = numberList[length - 1 - index]
    numberList[length - 1 - index] = numberList[index]
    numberList[index] = tempNumber
#    print(index, length - 1)
    index += 1
print(*numberList)

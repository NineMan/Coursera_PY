numberList = list(map(int, input().split()))

maxNumber = 0
maxCount = 0
for i in numberList:
    count = numberList.count(i)
    if count > maxCount:
        maxCount = count
        maxNumber = i
print(maxNumber)

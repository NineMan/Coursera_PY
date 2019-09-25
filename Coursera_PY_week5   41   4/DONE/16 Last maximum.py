numList = list(map(int, input().split()))

maxValue = numList[0]
maxIndex = 0

for i in range(len(numList)):
    if numList[i] >= maxValue:
        maxValue = numList[i]
        maxIndex = i
print(maxValue, maxIndex)

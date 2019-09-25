numberList = list(map(int, input().split()))

maxNumber = numberList[0]
maxIndex = 0

for i in range(len(numberList)):
    if numberList[i] > maxNumber:
        maxNumber = numberList[i]
        maxIndex = i
print(maxNumber, maxIndex)

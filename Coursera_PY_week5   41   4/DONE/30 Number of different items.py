numList = list(map(int, input().split()))

index = 0
prevNumber = numList[0]
sum = 1
while index < len(numList):
    if numList[index] != prevNumber:
        sum += 1
        prevNumber = numList[index]
    index += 1
print(sum)

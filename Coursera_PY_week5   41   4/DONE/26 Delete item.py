numList = list(map(int, input().split()))
index = int(input())

for i in range(len(numList)):
    if i == index:
        endNumber = numList[i]
    elif i > index and i != len(numList):
        numList[i - 1] = numList[i]
    elif i == len(numList):
        numList[i] = endNumber
numList.pop()
print(*numList)

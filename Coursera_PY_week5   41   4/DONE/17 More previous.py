numList = list(map(int, input().split()))

prevNumber = numList[0]

for i in numList:
    if i > prevNumber:
        print(i, end=" ")
    prevNumber = i

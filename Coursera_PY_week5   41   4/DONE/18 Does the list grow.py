def isAscending(fList):
    i = 1
    prevNumber = fList[0]
    length = len(fList)

    while (i != length) and (fList[i] > prevNumber):
        prevNumber = fList[i]
        i += 1
    return i == length


numList = list(map(int, input().split()))
answer = ('NO', 'YES')
print(answer[isAscending(numList)])

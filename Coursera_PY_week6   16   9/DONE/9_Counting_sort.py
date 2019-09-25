def CountSort(funcList):
    MyList = [0] * 101
    returnList = []
    for i in funcList:
        MyList[i] += 1
    for number in range(101):
        j = 0
        while j < MyList[number]:
            returnList.append(number)
            j += 1
    return returnList


numberList = list(map(int, input().split()))
print(*CountSort(numberList))

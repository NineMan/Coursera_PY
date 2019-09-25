def intersection(listA, listB):
    i = 0
    j = 0
    lenA = len(listA)
    lenB = len(listB)
    listC = []
    while (i < lenA) and (j < lenB):
        if listA[i] == listB[j]:
            listC.append(listA[i])
            i += 1
            j += 1
        elif listA[i] < listB[j]:
            i += 1
        elif listA[i] > listB[j]:
            j += 1
    return(listC)


numberListA = list(map(int, input().split()))
numberListB = list(map(int, input().split()))
# numberListA = [2, 4, 6, 8, 10]
# numberListB = [1, 3, 5, 7]

numberListC = intersection(numberListA, numberListB)
print(*numberListC)

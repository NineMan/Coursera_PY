def merge(listA, listB):
    i = 0
    j = 0
    lenA = len(listA)
    lenB = len(listB)
    listC = []
    while (i < lenA) and (j < lenB):
        if listA[i] <= listB[j]:
            listC.append(listA[i])
            i += 1
        elif listB[j] < listA[i]:
            listC.append(listB[j])
            j += 1
    if i == lenA:
        while j < lenB:
            listC.append(listB[j])
            j += 1
    elif j == lenB:
        while i < lenA:
            listC.append(listA[i])
            i += 1
    return(listC)


numberListA = list(map(int, input().split()))
numberListB = list(map(int, input().split()))
listC = merge(numberListA, numberListB)
print(*listC)

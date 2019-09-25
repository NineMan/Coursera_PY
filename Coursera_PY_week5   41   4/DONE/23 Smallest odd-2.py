numList = list(map(int, input().split()))

first = True
for i in numList:
    if i % 2 != 0:
        if first:
            first = False
            minOdd = i
        else:
            if i < minOdd:
                minOdd = i

print(minOdd)

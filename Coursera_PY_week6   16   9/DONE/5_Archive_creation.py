listA = list(map(int, input().split()))
freeSpace = listA[0]    # free space on server
n = listA[1]            # amount of number

listDataVolume = []
for i in range(n):
    listDataVolume.append(int(input()))

listDataVolume.sort()
lenght = len(listDataVolume)
sumSpace = 0
i = 0
while (sumSpace <= freeSpace) and (i < lenght):
    sumSpace += listDataVolume[i]
    if sumSpace <= freeSpace:
        i += 1
print(i)

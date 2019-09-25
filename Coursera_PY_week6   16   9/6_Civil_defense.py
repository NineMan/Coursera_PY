n = int(input())
listVillagesPos = list(map(int, input().split()))
m = int(input())
listBunkersPos = list(map(int, input().split()))

listVillages = []
for i in range(n):
    listVillages.append([listVillagesPos[i], i + 1])
listVillages.sort()

listBunkers = []
for i in range(m):
    listBunkers.append([listBunkersPos[i], i + 1])
listBunkers.sort()

i = 0
j = 1
if len(listBunkers) == 1:
    j = 0

while i < len(listVillages):
    nowBunker = listBunkers[j - 1]
    nextBunker = listBunkers[j]
    while (listBunkers[j][0] <= listVillages[i][0]) and j < (m - 1):
        nowBunker = listBunkers[j]
        j += 1
        nextBunker = listBunkers[j]
    delta1 = abs(nowBunker[0] - listVillages[i][0])
    delta2 = abs(nextBunker[0] - listVillages[i][0])
    if delta1 <= delta2:
        listVillages[i].append(nowBunker[1])
    else:
        listVillages[i].append((nextBunker[1]))
    i += 1

listVillages.sort(key=lambda x: x[1])

index = 0
while index < (len(listVillages) - 1):
    print(listVillages[index][2], end=' ')
    index += 1
print(listVillages[-1][2])

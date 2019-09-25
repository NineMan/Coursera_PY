numList = list(map(int, input().split()))

if 0 != numList[0] % 2:
    minOdd = numList[0]
else:
    i = 1
    while i < len(numList) and 0 == numList[i] % 2:
        i += 1
    minOdd = numList[i]

for i in range(len(numList)):
    if numList[i] < minOdd and (numList[i] % 2 != 0):
        minOdd = numList[i]

print(minOdd)

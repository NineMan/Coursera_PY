inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

listNumbers = []
for line in inFile:
    inputNumbers = tuple(map(str, line.split()))
    listNumbers.append(inputNumbers)

k = int(listNumbers[0][0])
listMembers = []
i = 1
while i < len(listNumbers):
    listTemp = []
    for j in range(-1, -4, -1):
        listTemp.append(int(listNumbers[i][j]))
    listMembers.append(listTemp)
    i += 1

listChallendger = []
for member in listMembers:
    if member[-3] >= 40 and member[-2] >= 40 and member[-1] >= 40:
        listChallendger.append(member[-3] + member[-2] + member[-1])
    i += 1

listChallendger.sort(reverse=True)
# print(*listChallendger)
lenght = len(listChallendger)
if k >= lenght:
    print(0, file=outFile)
elif listChallendger[0] == listChallendger[k]:
    print(1, file=outFile)
else:
    firstk = listChallendger.index(listChallendger[k - 1])
    if listChallendger[k - 1] == listChallendger[k]:
        print(listChallendger[firstk - 1], file=outFile)
    else:
        print(listChallendger[k - 1], file=outFile)

inFile.close()
outFile.close()

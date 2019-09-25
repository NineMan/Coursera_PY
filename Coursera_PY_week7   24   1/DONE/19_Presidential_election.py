inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

numberVotes = 0
presidentDict = {}
for line in inFile.readlines():
    president = line.strip()
    # print(president)
    if president not in presidentDict:
        presidentDict[president] = 0
    presidentDict[president] += 1
    # print(presidentDict)
    numberVotes += 1
# print(presidentDict)
# print(numberVotes)

sortedPresidentList = sorted(presidentDict, key=lambda a: -presidentDict[a])
# print(sortedPresidentList)

if presidentDict[sortedPresidentList[0]] * 2 > numberVotes:
    print(sortedPresidentList[0], file=outFile)
else:
    print(sortedPresidentList[0], file=outFile)
    print(sortedPresidentList[1], file=outFile)

inFile.close()
outFile.close()

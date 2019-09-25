inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

listParticipants = []
for line in inFile:
    tempList = list(map(str, line.split()))
    participant = [tempList[0], tempList[1], tempList[3]]
    listParticipants.append(participant)

listParticipants.sort()

for participant in listParticipants:
    print(' '.join(map(str, participant)), file=outFile)
#    print(*participant, file=outFile)
#    print(participant[0], participant[1], participant[2], file=outFile)

inFile.close()
outFile.close()

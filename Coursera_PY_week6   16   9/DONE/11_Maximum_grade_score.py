inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

listParticipants = []
for line in inFile:
    participant = tuple(map(str, line.split()))
    listParticipants.append(participant)

listClass = [9, 10, 11]
for number in listClass:
    listTemp = []
    for participant in listParticipants:
        if number == int(participant[2]):
            listTemp.append(participant[3])
    listTemp.sort(reverse=True)
    print(listTemp[0], end=' ', file=outFile)
    print(listTemp[0], end=' ')

inFile.close()
outFile.close()

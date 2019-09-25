inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

listMembers = []
for line in inFile:
    member = tuple(map(str, line.split()))
    listMembers.append(member)

listClass = [9, 10, 11]
for number in listClass:
    listTemp = []
    for member in listMembers:
        if number == int(member[2]):
            listTemp.append(member[3])
    listTemp.sort(reverse=True)
    countMembers = listTemp.count(listTemp[0])
    print(countMembers, end=' ', file=outFile)

inFile.close()
outFile.close()

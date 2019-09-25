inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

NUMBER_OF_SEATS = 450

depDict = {}
depList = []
votes = 0
for line in inFile.readlines():
    *a, b = line.strip().split()
    partyName = ' '.join(a)
    depDict[partyName] = int(b)
    depList.append(partyName)
    votes += int(b)

firstSQ = votes / NUMBER_OF_SEATS
sumSeats = 0
for party in depDict:
    seats = int(depDict[party] // firstSQ)
    remain = depDict[party] % firstSQ
    depDict[party] = [remain, int(depDict[party]), seats]
    sumSeats += seats

# def sortedParty(party[x]):
#     return (-party[x][0], -party[x][1])

sDepL = sorted(depDict, key=lambda x: (-depDict[x][0], -depDict[x][1]))
if int(sumSeats) != NUMBER_OF_SEATS:
    for i in range(NUMBER_OF_SEATS - int(sumSeats)):
        depDict[sDepL[i]][2] += 1

for party in depList:
    print(party, depDict[party][2], file=outFile)

inFile.close()
outFile.close()

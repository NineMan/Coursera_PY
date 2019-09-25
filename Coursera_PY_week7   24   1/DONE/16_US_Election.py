inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

candidateDict = {}
for line in inFile.readlines():
    candidate, votesCandidate = list(map(str, line.strip().split()))
    if candidate not in candidateDict:
        candidateDict[candidate] = 0
    candidateDict[candidate] += int(votesCandidate)

candidateList = sorted(candidateDict)
for index in candidateList:
    print(index, candidateDict[index], file=outFile)

inFile.close()
outFile.close()

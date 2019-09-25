inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

wordsDict = {}
for line in inFile.readlines():
    wordList = list(map(str, line.strip().split()))
    # print(wordList)
    for word in wordList:
        if word not in wordsDict:
            wordsDict[word] = 0
        print(wordsDict[word], end=' ', file=outFile)
        wordsDict[word] += 1

inFile.close()
outFile.close()

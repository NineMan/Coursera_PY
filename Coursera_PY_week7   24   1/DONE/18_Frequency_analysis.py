inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

wordDict = {}
for line in inFile.readlines():
    wordList = list(map(str, line.strip().split()))
    for word in wordList:
        if word not in wordDict:
            wordDict[word] = 0
        wordDict[word] += 1

sortedList = sorted(wordDict, key=lambda x: (-wordDict[x], x))
for word in sortedList:
    print(word, file=outFile)

inFile.close()
outFile.close()

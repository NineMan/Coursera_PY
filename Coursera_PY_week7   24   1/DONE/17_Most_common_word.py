inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

wordDict = {}
for line in inFile.readlines():
    wordList = list(map(str, line.strip().split()))
    for word in wordList:
        if word not in wordDict:
            wordDict[word] = 0
        wordDict[word] += 1

sortedWordDict = sorted(wordDict, key=lambda x: (-wordDict[x], x))
print(sortedWordDict[0], file=outFile)

# for word in sorted(wordDict):
#     print(word, wordDict[word], file=outFile)

inFile.close()
outFile.close()

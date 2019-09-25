fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

number = int(fin.readline())
dictSet = set()
wordSet = set()
for _ in range(number):
    word = fin.readline().strip()
    dictSet.add(word)
    wordSet.add(word.lower())

testList = fin.readline().split()
mistakes = 0
for word in testList:
    if word.lower() in wordSet:
        if word not in dictSet:
            mistakes += 1
    else:
        up = 0
        for i in word:
            if i.isupper():
                up += 1
        if up != 1:
            mistakes += 1
print(mistakes, file=fout)

fin.close()
fout.close()

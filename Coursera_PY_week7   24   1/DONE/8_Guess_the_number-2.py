hiddenSet = set(range(int(input()) + 1))
hiddenSet.remove(0)

line = input()
answerList = []
while line != 'HELP':
    questionSet = set(map(int, line.split()))
    if len(hiddenSet & questionSet) * 2 <= len(hiddenSet):
        answerList.append('NO')
        hiddenSet = hiddenSet - questionSet
    else:
        answerList.append('YES')
        hiddenSet = hiddenSet & questionSet
    line = input()

for answer in answerList:
    print(answer)

hiddenList = list(hiddenSet)
hiddenList.sort()
print(*hiddenList)

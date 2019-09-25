hiddenSet = set(range(int(input()) + 1))
hiddenSet.remove(0)

line = str(input())

while line != 'HELP':
    answerSet = set(map(int, line.split()))
    answer = str(input())
    if answer == 'YES':
        hiddenSet &= answerSet
    elif answer == 'NO':
        hiddenSet -= answerSet
    line = str(input())
hiddenList = list(hiddenSet)
hiddenList.sort()
print(*hiddenList)

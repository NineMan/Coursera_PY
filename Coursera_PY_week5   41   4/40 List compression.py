numList = list(map(int, input().split()))
# numList = [5, 0, 4, 0, 3, 0, 0, 2]

sum = 0
lenght = len(numList)
for i in range(lenght):
    if numList[i] != 0:
        numList.append(numList[i])
    else:
        sum += 1
for i in range(sum):
    numList.append(0)
numList.reverse()
for i in range(lenght):
    numList.pop()
numList.reverse()

print(*numList)

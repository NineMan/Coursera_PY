numberList = list(map(int, input().split()))

if len(numberList) > 1:
    prevNumber = numberList[1]
prevPrevNumber = numberList[0]
sum = 0
lenght = len(numberList)
for i in range(2, lenght):
    if prevPrevNumber < prevNumber > numberList[i]:
        sum += 1
    prevPrevNumber = prevNumber
    prevNumber = numberList[i]
print(sum)

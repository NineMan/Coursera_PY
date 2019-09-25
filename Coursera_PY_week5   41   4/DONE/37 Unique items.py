numberList = list(map(int, input().split()))

# i = 0
# while i < len(numberList):
#    sum = 0
#    j = 0
#    while j < len(numberList):
#        if numberList[i] == numberList[j]:
#            sum += 1
#        j += 1
#    if sum == 1:
#        print(numberList[i], end=' ')
#    i += 1

for i in numberList:
    if numberList.count(i) == 1:
        print(i, end=' ')

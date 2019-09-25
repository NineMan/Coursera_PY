numberList = list(map(int, input().split()))

sum = 0
for i in numberList:
    sum += numberList.count(i) - 1
print(int(sum / 2))

####################################################
# sum = 0
# for i in range(len(numberList)):
#    for j in range(i + 1, len(numberList)):
#        if numberList[i] == numberList[j]:
#            sum += 1
# print(sum)
#
####################################################
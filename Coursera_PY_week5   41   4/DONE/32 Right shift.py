numList = list(map(int, input().split()))
numList1 = numList[:]
# version 1
print(*(numList[-1:]+ numList[:-1]))

# version 2

numList.insert(0, numList[-1])
numList.pop()
print(*numList)

# version 3

first = numList1[-1]
old = numList1[0]
for i in range(len(numList1)):
    new = numList1[i]
    numList1[i] = old
    old = new
numList1[0] = first
print(*numList1)

numList = list(map(int, input().split()))

i = 1
while i < len(numList):
    neighborPositie = numList[i] > 0 and numList[i - 1] > 0
    neighborNegative = numList[i] < 0 and numList[i - 1] < 0
    if neighborPositie or neighborNegative:
        print(numList[i - 1], numList[i], sep=' ')
        i = len(numList)
    i += 1

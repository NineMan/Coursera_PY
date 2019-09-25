n = int(input())
numList = list(map(int, input().split()))
x = int(input())

minDelta = 2001
for i in numList:
    delta = ((x - i) ** 2) ** 0.5
    if delta < minDelta:
        minDelta = delta
        leastNumber = i

print(leastNumber)

numList = list(map(int, input().split()))

minPositiv = 1000
for i in numList:
    if i < minPositiv and i > 0:
        minPositiv = i
print(minPositiv)

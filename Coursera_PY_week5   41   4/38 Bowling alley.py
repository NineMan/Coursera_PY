numList = list(map(int, input().split()))
n = numList[0]
k = numList[1]

#kegleList = list(range(numList[0]))
throwList = tuple(range(k))

#print(kegleList)
#print(throwList)

for i in range(k):
    throwList[i] = list(map(int, input().split()))

print(throwList)

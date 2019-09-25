n = int(input())

partSum = 0
totalSum = n
for i in range(1, n):
    a = int(input())
    totalSum += i
    partSum += a
print(totalSum - partSum)

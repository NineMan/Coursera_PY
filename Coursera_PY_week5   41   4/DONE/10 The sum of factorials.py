n = int(input())

partFactorial = 1
sumFactorial = 0
for i in range(1, n + 1):
    partFactorial *= i
    sumFactorial += partFactorial
print(sumFactorial)

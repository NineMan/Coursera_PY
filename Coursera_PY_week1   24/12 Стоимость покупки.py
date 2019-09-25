a = int(input())
b = int(input())
n = int(input())

r = (n * (a * 100 + b)) // 100
k = (n * (a * 100 + b)) % 100
print(r, k)

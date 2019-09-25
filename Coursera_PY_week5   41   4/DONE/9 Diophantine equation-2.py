a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

root = 0
for x in range(1001):
    numerator = a * x ** 3 + b * x ** 2 + c * x + d
    denominator = x - e
    if denominator != 0 and numerator / denominator == 0:
        root += 1
print(root)

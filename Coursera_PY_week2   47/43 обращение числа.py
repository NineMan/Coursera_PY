n = int(input())

new = 0
while (n != 0):
    new = new * 10 + (n % 10)
    n = n // 10
print(new)

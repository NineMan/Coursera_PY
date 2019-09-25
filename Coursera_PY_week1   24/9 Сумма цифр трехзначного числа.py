x = int(input())
c = x % 10          # единицы
b = (x // 10) % 10  # десятки
a = x // 100        # сотни
print(a + b + c)

a1234 = int(input())

a4 = a1234 % 10
a123 = a1234 // 10
a3 = a123 % 10
a12 = a123 // 10
a2 = a12 % 10
a1 = a12 // 10

y = int(int(a1 == a4) & int(a2 == a3))

print(y)

x = int(input())
minut = x % (24 * 60)
h = minut // 60
m = minut % 60
print(h, m)

v = int(input())
t = int(input())
s = v * t
km = s % 109
#km = (109 + (v * t) % 109) % 109
print(km)

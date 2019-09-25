import math

x = float(input())

if x - int(x) == 0.5:
    result = math.ceil(x)
else:
    result = round(x)

print(result)

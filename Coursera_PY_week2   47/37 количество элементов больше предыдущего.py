x = int(input())

prev = x
num = 0
while(x != 0):
    if(x > prev):
        num = num + 1
    prev = x
    x = int(input())
print(num)

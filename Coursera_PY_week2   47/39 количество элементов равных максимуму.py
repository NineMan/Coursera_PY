x = int(input())

max1 = 0
n = 0
while(x != 0):
    if(x > max1):
        max1 = x
        n = 1
    elif(x == max1):
        n = n + 1
    x = int(input())
print(n)

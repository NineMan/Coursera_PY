myList = list(map(int, input().split()))

mySetFin = set()
lenghtPrev = -1


for num in myList:
    mySetFin.add(num)
    lenghtNow = len(mySetFin)
    if lenghtPrev == lenghtNow:
        print('YES')
        lenghtPrev = lenghtNow
    else:
        print('NO')
        lenghtPrev = lenghtNow

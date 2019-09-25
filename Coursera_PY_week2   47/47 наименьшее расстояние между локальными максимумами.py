nNow = int(input())

nPrev = nNow
nPrevPrev = nNow
lengthMax = 0
lengthMaxMin = 0
n = 0

while nNow != 0:
    if nPrev > nNow and nPrev >= nPrevPrev:
        if n == 0:
            n = 1
        elif n == 1:
            lengthMaxMin = lengthMax
            n = 2
        else:
            if lengthMaxMin > lengthMax:
                lengthMaxMin = lengthMax
        lengthMax = 0
    lengthMax += 1
    nPrevPrev = nPrev
    nPrev = nNow
    nNow = int(input())

print(lengthMaxMin)

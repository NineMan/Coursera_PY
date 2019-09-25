a1, a2 = int(input()), int(input())
b1, b2 = int(input()), int(input())
c1, c2 = int(input()), int(input())

#  Сравниваю все пары (спички) между собой 1.
compAB = (a1 <= b2 and b1 <= a2)
compBC = (b1 <= c2 and c1 <= b2)
compAC = (a1 <= c2 and c1 <= a2)

aa1 = a1 - (b2 - b1)
aa2 = a2 + (b2 - b1)
bb1 = b1 - (c2 - c1)
bb2 = b2 + (c2 - c1)
cc1 = c1 - (a2 - a1)
cc2 = c2 + (a2 - a1)

if (compAB and compBC) or (compBC and compAC) or (compAB and compAC):
    print(0)
#  Добавляю одну спичку к другим (3 варианта) и сравниваю 2 новых отрезка
#  Если пересекаются - то гуд.
elif (b1 <= cc2 and b2 >= c1) or (b1 <= c2 and b2 >= cc1):
    print(1)
elif (a1 <= c2 and aa2 >= c1) or (aa1 <= c2 and a2 >= c1):
    print(2)
elif (a1 <= bb2 and a2 >= b1) or (a1 <= b2 and a2 >= bb1):
    print(3)
else:
    print(-1)

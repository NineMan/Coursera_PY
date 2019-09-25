a = int(input())

dec = a // 10
ed = a % 10

if (dec == 1):
    print(a, 'korov')
elif (ed == 0):
    print(a, 'korov')
elif (ed == 5):
    print(a, 'korov')
elif (ed == 6) or (ed == 7) or (ed == 8) or (ed == 9):
    print(a, 'korov')
elif (ed == 1):
    print(a, 'korova')
else:
    print(a, 'korovy')

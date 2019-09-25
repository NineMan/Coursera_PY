a = int(input())

f_n_1 = 0
f_n_2 = 1
f_n = 1
i = 0

if a == 0:
    print(0)
elif a == 1:
    print(1)
else:
    while(f_n < a):
        f_n = f_n_1 + f_n_2
        f_n_2 = f_n_1
        f_n_1 = f_n
        i = i + 1
    if f_n_1 == a:
        print(i)
    else:
        print(-1)

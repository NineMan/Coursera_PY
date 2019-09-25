x = int(input())

f_n_1 = 0
f_n_2 = 1
i = 0

if x == 0:
    print(0)
elif x == 1:
    print(1)
else:
    while(i != x):
        f_n = f_n_1 + f_n_2
        f_n_2 = f_n_1
        f_n_1 = f_n
        i = i + 1
    print(f_n)

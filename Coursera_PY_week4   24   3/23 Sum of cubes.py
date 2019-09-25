def func(n, count = 0):
    if n == 0:
        return count
    else:

        k = func (n - 1, count + 1)
        return k


n = int(input())
print('функция возвратила: ', func(n, 1))

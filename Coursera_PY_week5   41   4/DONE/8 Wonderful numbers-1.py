for i in range(10, 100):
    dec = i // 10
    num = i % 10
    if i == (2 * dec * num):
        print(i)
    print(i, dec, num, 2 * dec * num)

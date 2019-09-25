a = '2 3 0 -4'
number = map(int, a.split())
#################################
# sum()         # print(sum(number))
# max()
# min()
# map()
# sorted()
# filter()      # print(*filter(lambda x: x > 0, map(int, a.split())))
# enumerate():
                # print(*enumerate(number))

                # f = open('input.txt', 'r', encoding='utf8')
                # for i, line in enumerate(f, 1):
                #     if line.strip() == '':
                #         print('Blank line at line', i)

# any()
# all()         # print(all(map(lambda x: abs(int(x)) <= 100, input().split())))
# zip()
b = zip(number, number)
print(list(b))

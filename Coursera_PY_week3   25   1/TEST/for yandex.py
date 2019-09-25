#  1 and 3
list = input().split(' ')
print(int(list[0]) + int(list[1]))

#f2 = open("input_1.txt", 'w')
#  2

#f = open('C:\Users\Dell\YandexDisk\___Programming\PycharmProjects\Coursera_PY_week3\input.txt')
#fd = f.read()
#print(fd)
#open(r'C:\Users\Dell\YandexDisk\___Programming\PycharmProjects\Coursera_PY_week3\input.txt', 'r')


handle = open("input.txt", "r")
data = handle.read()
handle.close()

position = data.find(' ')
a = int(data[:position])
b = int(data[position + 1:])
f1 = open('output.txt', 'w')
f1.write(str(a + b))

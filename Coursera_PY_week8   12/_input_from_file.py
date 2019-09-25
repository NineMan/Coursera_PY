import sys

# чтение файла построчно (через for):

# for line in sys.stdin:
#     print(line, end='')

##############################################

# метод read() читает файл целиком:
# / в конце нажать Ctrl+D

# print(sys.stdin.read().strip().split())

##############################################

# f = open('input.txt', 'r', encoding='utf8')
# for i, line in enumerate(f, 1):
#     if line.strip() == '':
#         print('Blank line at line', i)

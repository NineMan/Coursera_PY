import os


def lineCounting(fileName):
    file = open(fileName)
    x = file.readlines()
    lines = len(x)
    return lines


path = os.listdir(path=".")
pathPY = []
for i in path:
    if i[-3:] == '.py':
        pathPY.append(i)

sum = 0
for i in pathPY:
    linesInFile = lineCounting(i)
    sum += linesInFile
    print('{: >2} lines in "{}"'.format(linesInFile, i))
sum -= lineCounting('Line counting.py')
print('TOTAL lines =', sum)

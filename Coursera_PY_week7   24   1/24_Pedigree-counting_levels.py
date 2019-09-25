fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

number = int(fin.readline())
treeDict = {}
for line in fin:
    child, parent = line.strip().split()
    treeDict[child] = parent

print(treeDict)

fin.close()
fout.close()
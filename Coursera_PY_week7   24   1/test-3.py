fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

for line in fin:
    command, *other = line.strip().split()
    print(command, ' - ', other)

fin.close()
fout.close()
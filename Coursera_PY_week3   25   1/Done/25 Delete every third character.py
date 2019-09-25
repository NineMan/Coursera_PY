openFile = open("input.txt", "r")
string = openFile.read()
openFile.close()
#string = input()

i = 0
while i < len(string):
    string = string.replace(string[i], '', 1)
    i += 2

#print(string)
writeFile = open('output.txt', 'w')
writeFile.write(string)

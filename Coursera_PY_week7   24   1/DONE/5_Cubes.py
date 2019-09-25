inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

lines = inFile.readlines()

numberAnn = list(map(int, lines[0].split()))[0]
numberBoris = list(map(int, lines[0].split()))[1]

setAnnCubes = set()
for line in lines[1:numberAnn + 1]:
    setAnnCubes.add(int(line))

setBorisCubes = set()
for line in lines[numberAnn + 1:]:
    setBorisCubes.add(int(line))

setAllCubes = setAnnCubes & setBorisCubes
listAllCubes = list(setAllCubes)
listAllCubes.sort()

setOnlyAnnCubes = setAnnCubes - setBorisCubes
listOnlyAnnCubes = list(setOnlyAnnCubes)
listOnlyAnnCubes.sort()

setOnlyBorisCubes = setBorisCubes - setAnnCubes
listOnlyBorisCubes = list(setOnlyBorisCubes)
listOnlyBorisCubes.sort()

print(len(listAllCubes), file=outFile)
print(*listAllCubes, file=outFile)
print(len(listOnlyAnnCubes), file=outFile)
print(*listOnlyAnnCubes, file=outFile)
print(len(listOnlyBorisCubes), file=outFile)
print(*listOnlyBorisCubes, file=outFile)

inFile.close()
outFile.close()

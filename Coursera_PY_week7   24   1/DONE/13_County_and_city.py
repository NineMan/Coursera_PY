inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')

num = int(inFile.readline())
countryDict = {}
for country in range(num):
    countryList = list(map(str, inFile.readline().split()))
    nameCountry = countryList[0]
    for city in range(1, len(countryList)):
        countryDict[countryList[city]] = nameCountry

numCity = int(inFile.readline())
cityListAnswer = []
for i in range(numCity):
    city = inFile.readline().strip()
    cityListAnswer.append(countryDict[city])

for country in cityListAnswer:
    print(country, file=outFile)

inFile.close()
outFile.close()

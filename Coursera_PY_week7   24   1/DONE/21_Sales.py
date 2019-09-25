fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

mainDict = {}
for line in fin:
    lineList = line.strip().split()
    customer = lineList[0]
    product = lineList[1]
    quantity = int(lineList[2])

    mainDict[customer] = mainDict.get(customer, {})
    mainDict[customer][product] = mainDict[customer].get(product, 0) + quantity

    # if customer not in mainDict:
    #     mainDict[customer] = {}
    # if product not in mainDict[customer]:
    #     mainDict[customer][product] = 0
    # mainDict[customer][product] += quantity

for customer in sorted(mainDict):
    print(customer + ':')
    for product in sorted(mainDict[customer]):
        print(product, mainDict[customer][product])

fin.close()
fout.close()

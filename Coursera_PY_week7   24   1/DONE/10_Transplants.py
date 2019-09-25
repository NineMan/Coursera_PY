listStation = list(map(int, input().split()))
# listStation = [3, 6, 5, 10]

listBusStation1 = listStation[:2]
listBusStation2 = listStation[2:]
listBusStation1.sort()
listBusStation2.sort()

setBusStation1 = set(range(listBusStation1[0], listBusStation1[1] + 1))
setBusStation2 = set(range(listBusStation2[0], listBusStation2[1] + 1))

# print(setBusStation1)
# print(setBusStation2)
# print(setBusStation1 & setBusStation2)

print(len(setBusStation1 & setBusStation2))

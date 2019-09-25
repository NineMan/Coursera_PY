#n = list(map(int, input().split()))
#listVillages = list(map(int, input().split()))
#m = list(map(int, input().split()))
#listShelters = list(map(int, input().split()))
#############################
# version 1
n = 4
m = 2
#listVillages = [1, 2, 6, 10]
#listShelters = [7, 3]
#############################
# version 2
# n = 1
# m = 1
# listVillages = [1]
# listShelters = [2]
#############################
# version 3
# n = 10
# m = 10
# listVillages = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]
# listShelters = [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]
#############################

#listVillagesPos = []
#for i in range(n):
#    listVillagesPos.append((listVillages[i], i + 1))
#listVillagesPos.sort()
#print(" ".join(map(str, listVillagesPos)))

#listSheltersPos = []
#for i in range(m):
#    listSheltersPos.append((listShelters[i], i + 1))
#print(*listSheltersPos)
#listSheltersPos.sort()
listVillagesPos = [(1, 1), (2, 2), (6, 3), (10, 4)]
listVillagesPos.sort()
listSheltersPos = [(7, 1), (3, 2)]
listSheltersPos.sort()
#print(*listVillagesPos)
#print(*listSheltersPos)






#j = 0
#lenght = len(listSheltersPos)
#for i in listVillagesPos:
#    while (j < lenght) and (listSheltersPos[j][0] < i[0]):
#        print('[j][0] и i[0] = ', listSheltersPos[j][0], i[0], end=' ')
#        j += 1
#    print('j =', j, end=' ')
#    print(i[0])

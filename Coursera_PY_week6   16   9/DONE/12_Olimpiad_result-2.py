# inFile = open('input.txt', 'r', encoding='utf8')
# outFile = open('output.txt', 'w', encoding='utf8')


def maxScore(member):
    return int(member[1])


n = int(input())
listMembers = []

# for line in inFile:
#     member = tuple(map(str, line.split()))
#     listMembers.append(member)

for index in range(n):
    member = tuple(map(str, input().split()))
    listMembers.append(member)

listMembers.sort()
listMembers.sort(reverse=True, key=maxScore)

for member in listMembers:
    print(member[0])
#    print(member[0], file=outFile)

# inFile.close()
# outFile.close()

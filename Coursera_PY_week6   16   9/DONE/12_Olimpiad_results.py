n = int(input())
listMembers = []

for index in range(n):
    member = tuple(map(str, input().split()))
    listMembers.append(member)
listMembers.sort(key=lambda x: int(x[1]), reverse=True)

for member in listMembers:
    print(member[0])

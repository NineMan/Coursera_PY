n = int(input())

myDict = {}
for i in range(n):
    word, synonym = map(str, input().split())
    myDict[word] = synonym
    myDict[synonym] = word
print(myDict[input()])

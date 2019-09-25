numList = list(map(int, input().split()))
heightPetya = int(input())

index = 0
while index < len(numList) and heightPetya <= numList[index]:
    index += 1
print(index + 1)

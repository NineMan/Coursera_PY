# mySet1 = set(map(int, input().split()))
# mySet2 = set(map(int, input().split()))
# print(*sorted(mySet1 & mySet2))

print(*sorted(map(int, (set(input().split()) & set(input().split())))))

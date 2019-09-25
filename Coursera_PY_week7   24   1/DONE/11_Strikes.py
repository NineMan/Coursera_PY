numberDay, numberParty = map(int, input().split())

# version 1
# setWeekEnds = set()
# setWeekEnds |= set(range(6, numberDay + 1, 7))
# setWeekEnds |= set(range(7, numberDay + 1, 7))

setWeekEnds = {i for i in range(1, numberDay + 1) if i % 7 in [0, 6]}

setStrikesDay = set()
for _ in range(numberParty):
    start, step = map(int, input().split())
    setStrikesDay |= set(range(start, numberDay + 1, step))

setStrikesDay = setStrikesDay - setWeekEnds
# print(*setStrikesDay)
print(len(setStrikesDay))

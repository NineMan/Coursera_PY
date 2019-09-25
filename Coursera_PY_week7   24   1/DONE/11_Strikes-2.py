days, numberPartys = map(int, input().split())

strikes = set()
strikesAll = set()
for _ in range(numberPartys):
    a, b = map(int, input().split())
#     альтернативный вариант
#     strikes = {i for i in range(a, days + 1, b) if i % 7 != 0 and i % 7 != 6}
    strikes = {i for i in range(a, days + 1, b) if i % 7 not in [0, 6]}
    strikesAll |= strikes

# print(*strikesAll)
print(len(strikesAll))

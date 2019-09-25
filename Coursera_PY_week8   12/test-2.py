pas = map(int, input().split())
# pas = [1, 2]
sortedPas = sorted(enumerate(pas), key=lambda x: x[1])

taxi = map(int, input().split())
# taxi = [20, 10]
sortedTaxi = sorted(enumerate(taxi), key=lambda x: x[1], reverse=True)

ans = tuple(zip(sortedPas, sortedTaxi))
sortedAns = sorted(ans, key=lambda x: x[0][0])
print(*map(lambda x: x[1][0] + 1, sortedAns))

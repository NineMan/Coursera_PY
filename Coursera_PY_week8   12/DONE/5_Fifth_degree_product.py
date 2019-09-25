from sys import stdin
from functools import reduce

print(
    reduce(
        lambda x, y: x * y ** 5,
        map(
            int,
            stdin.read().strip().split()
        ),
        1
    )
)

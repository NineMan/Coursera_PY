from sys import stdin
print(
    len(
        set(
            stdin.read().strip().split()
        )
    )
)

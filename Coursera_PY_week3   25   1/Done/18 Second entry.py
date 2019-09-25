string = input()
substring = 'f'

pos = string.find(substring)
if pos == -1:
    print(-2)
else:
    pos = string.find(substring, pos + 1)
    if pos == -1:
        print(-1)
    else:
        print(pos)

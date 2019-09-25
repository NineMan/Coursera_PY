import sys

text = sys.stdin.read()
mySet = set(map(str, text.split()))
numberWords = len(mySet)

print(numberWords)

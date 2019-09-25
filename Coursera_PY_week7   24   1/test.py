array_of_sets = [{'a', 'b', 'c'}, {'a', 'c', 'd', 'e'}, {'a', 'y', 'z'}]

x = array_of_sets[0]
y = array_of_sets[0]
n = array_of_sets[0]
m = array_of_sets[0]

for i in array_of_sets:
    x &= i
    print(x)
    y |= i
    print(y)
    n = n & i
    print(n)
    m = m | i
    print(m)
    print('---------------')

print(x, y)
print(n, m)
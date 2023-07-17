list1 = ['2', '5', '6', '7']

print([int(x) for x in list1])
print(list(int(x) for x in list1))
# print(*(int(x) for x in list1))

def g(x):
    return int(x)**2

print([g(x) for x in list1])

print([g(x) for x in list1 if int(x) % 2 == 1])


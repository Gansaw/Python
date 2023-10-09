d = {
    'Park': 12345,
    'Kim': 234234,
    'Lee': 239084023
}

# for key, value in d.items():
#     print('{}: {}'.format(key, value))

for i, (key, value) in enumerate(d.items()):
    print('{}번째: {} - {}'.format(i, key, value))

    


a, b, c = (1, 2, 3)
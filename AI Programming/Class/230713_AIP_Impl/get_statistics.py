count = 0
total = 0

print('Enter -1 to terminate')
num = int(input('Enter a nonnegative integer: '))
min_val = num
max_val = num

while num != -1:
    count += 1
    total += num

    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    num = int(input('Enter a nonnegative integer: '))

if count > 0:
    if count >= 5:
        print('{}개임'.format(count))
    print('min: ', min_val)
    print('max: ', max_val)
    print('avg: ', total / count)
else:
    print('No numbers were entered!')

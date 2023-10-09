import time

digit_sum = 0

t0 = time.time()
for num in range(1, 1000001):
    # 12486 -> 1+2+4+8+6
    # for d in str(num):
    #     digit_sum += int(d)
    # digits = eval(list(str(num)))
    digit_sum += sum(int(d) for d in str(num))
    
t1 = time.time()

print('Sum: {}'.format(digit_sum))

print('Elapsed time: {}'.format(t1 - t0))



# digit_sum = 0
# for num in range(1, 10000001):
#     # 12486 -> 1+2+4+8+6
#     while num > 0:
#         digit = num % 10
#         digit_sum += digit
#         num //= 10

# print('Sum: {}'.format(digit_sum))
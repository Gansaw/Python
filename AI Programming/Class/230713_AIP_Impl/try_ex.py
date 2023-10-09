
try:
    num = int(input('Enter a number: '))
    print('Entered number: {}'.format(num))
except ValueError as exp:
    print('Error!!!')
    print('Error message: {}'.format(exp))
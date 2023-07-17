f = eval(input('Enter a future value: '))
r = eval(input('Enter interest rate (as %): '))
n = eval(input('Enter number of years: '))

present_value = f / (1 + r / 100) ** n

print('Present value: ${:,.2f}'.format(present_value))
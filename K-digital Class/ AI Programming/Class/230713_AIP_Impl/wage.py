# def main():
#     first_name, last_name, salary = get_input()
#     new_salary = calculate_salary(salary)

#     print('New salary for {} {}: ${:,.2f}'.format(
#         first_name, last_name, new_salary
#         ))

def get_input():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    salary = float(input('Enter current salary: '))

    return first_name, last_name, salary

def calculate_salary(salary):
    if salary <= 40000:
        new_salary = salary*1.05
    else:
        new_salary = salary + 2000 + (salary - 40000)*0.02

    return new_salary

# main()

first_name, last_name, salary = get_input()
new_salary = calculate_salary(salary)

print('New salary for {} {}: ${:,.2f}'.format(
    first_name, last_name, new_salary
    ))
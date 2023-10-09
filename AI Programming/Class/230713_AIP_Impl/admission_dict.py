d = {
    'child': 0,
    'minor': 5,
    'adult': 10,
    'senior': 8,
    'alien': 100
}

def main():
    # print('Enter the group')
    print('Option:')
    for k in d:
        print(k)
    group = input('Enter the group: ')
    # group = input('(child, minor, adult, or senior): ')

    print('Admission fee is:', determineAdmissionFee(group))

def determineAdmissionFee(group):
    # return d.get(group, 10000)
    return d[group]

main()

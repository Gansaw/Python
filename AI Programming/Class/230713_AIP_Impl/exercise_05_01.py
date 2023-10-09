def main():
    dict_unit = readUnits()

    print('UNITS OF LENGTH')

    for i, unit in enumerate(dict_unit):
        print('{:<15}'.format(unit), end='')
        if (i+1) % 3 == 0:
            print()

    unit_from, unit_to, length = getInput()

    length_converted = convertUnits(unit_from, unit_to, length, dict_unit)

    print('Length in {}: {:.4f}'.format(unit_to, length_converted))


def convertUnits(unit_from, unit_to, length, dict_unit):
    return length * dict_unit[unit_from] / dict_unit[unit_to]
    # return length * dict_unit.get(unit_from, 0) / dict_unit.get(unit_to, 1)

def readUnits():
    file_unit = open('Units.txt', 'r')

    dict_unit = {}
    for line in file_unit:
        name, value = line.split(',')
        dict_unit[name] = float(value)

    file_unit.close()

    return dict_unit


def getInput():
    unit_from = input('Unit to convert from: ')
    unit_to = input('Unit to convert to: ')
    length = float(input('Enter length in {}: '.format(unit_from)))

    return unit_from, unit_to, length


main()
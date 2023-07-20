def find_two_numbers(num):
    if len(num) == 1:
        return num

    if len(num) >= 2:
        num_sorted = sorted(num)
        first_num = num_sorted[-1]
        second_num = num_sorted[-2]
        return [first_num, second_num]

def main():
    num = list(map(int, input("input numbers: ").split()))
    result = find_two_numbers(num)
    print(result)

main()
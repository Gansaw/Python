import random

def main():
    # for _ in range(3):
    #     outcome = spinWheel()
    #     print(outcome, end="  ")

    num = 10000000
    dict_cnt = {}
    for _ in range(num):
        outcome = spinWheel()
        dict_cnt[outcome] = dict_cnt.get(outcome, 0) + 1

    for k, v in dict_cnt.items():
        print('{}: {} ({})'.format(k, v, v/num))

def spinWheel():
    n = random.randint(1, 20)
    if n > 15:
        return "Cherries"
    elif n > 10:
        return "Orange"
    elif n > 5:
        return "Plum"
    elif n > 2:
        return "Melon"
    elif n > 1:
        return "Bell"
    else:
        return "Bar"

main()
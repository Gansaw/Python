def calculateArray(arr, sum):
    sort_arr = sorted(arr)
    for i in range(len(sort_arr)):
        total = 0
        for j in range(i, len(sort_arr)):
            total += arr[j]
            if total == sum:
                return [i+1,j+1]
    return [-1]       


def main():
    arr = list(map(int, input("input number array: ").split()))
    sum = int(input("input sum what you want to find: "))
    result = calculateArray(arr, sum)
    print(result)


main()
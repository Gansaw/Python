def sort_binary_array(arr):
    arr0 = []
    arr1 = []

    for i in range(len(arr)):        
        if arr[i] == 0:
            arr0.append(arr[i])
        elif arr[i] == 1:
            arr1.append(arr[i])
        else:
            print("You can only enter 0 or 1")
            return None
            
    return arr0 + arr1


def main():
    arr = list(map(int, input("enter 0 or 1 array: ").split()))
    result = sort_binary_array(arr)
    print(result)

main()
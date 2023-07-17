# regions = [('aa', 1), ('bb', 2), ('cc', 3), ('dd', 4)]
# array = [['1', 2], ['3', 4]]

def sum_array(array):
    v1 = 0
    v2 = 0
    for e in array:
        v1 += int(e[0])
        v2 += e[1]
    return (str(v1), v2)

array = [('1', 2), ('3', 4), ('5', 6)]

print(sum_array(array)) # ('9', 12)




# print(sum(array))

# # print(array[0] + array[1]) # -> ['4', 6]

# print(regions[0]) 

# print(regions[0][1])

# print(regions[2][0])

# print(regions[2][1])
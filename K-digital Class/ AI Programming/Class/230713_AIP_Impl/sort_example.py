list1 = ('white', 'blue', 'red')
list2 = sorted(list1)
print(list2)
print(sorted(list1, reverse=True))
print(sorted(list1, key=len))
print(list1)
print(sorted('spam'))







# def main():
#     list1 = [
#         'democratic', 'sequoia',
#         'equals', 'brrr', 'break',
#         'two'
#     ]
#     list1.sort(key=len)
#     print('Sorted by length in ascending order:')
#     print(list1, '\n')
#     list1.sort(key=numberOfVowels, reverse=True)
#     print('Sorted by number of vowels in descending order:')
#     print(list1)

# def numberOfVowels(word):
#     vowels = 'aeiou'
#     total = 0
#     for vowel in vowels:
#         total += word.lower().count(vowel)
#     return total

# main()
          
word = input('Enter a word: ')
# reversedWord = ''

# 문제: 끝의 2개 글자만 순서 바꾸기
# abcde -> abced
reversedWord = word[:-2] + word[-1:-3:-1]
print(reversedWord)



# for ch in word:
#     reversedWord = ch + reversedWord
# print(reversedWord)

# print(word[::-1])

# print(''.join(list(reversed(word))))


word = input('Enter word to translate: ')

if word[0] in 'aeiouAEIOU':
    result = word + 'way'
else:
    for i in range(len(word)):
        if word[i] in 'aeiouAEIOU':
            result = word[i:] + word[:i] + 'ay'
            break

print('The word in Pig Latin is {}'.format(result))
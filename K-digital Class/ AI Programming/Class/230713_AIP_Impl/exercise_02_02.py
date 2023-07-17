sentence = input('Enter a sentence: ')
word1 = input('Enter a word to replace: ')
word2 = input('Enter replacement word: ')

words = sentence.split()
replaced = []

for w in words:
    if w == word1:
        w = word2
    replaced.append(w)

# replaced = sentence.replace(word1, word2)

replaced = ' '.join(replaced)
print(replaced)
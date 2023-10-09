def main():
    listOfWords = formListOfWords('Gettysburg.txt')
    freq = createFrequencyDictionary(listOfWords)
    displayWordCount(listOfWords, freq)
    displayMostCommonWords(freq)

def formListOfWords(fileName):
    infile = open(fileName)
    originalLine = infile.readline().lower()
    infile.close()

    line = ''
    for ch in originalLine:
        if ('a' <= ch <= 'z') or (ch == ' '):
            line += ch

    listOfWords = line.split()
    return listOfWords

def createFrequencyDictionary(listOfWords):
    freq = {}
    # for word in listOfWords:
    #     freq[word] = 0
    for word in listOfWords:
        freq[word] = freq.get(word, 0) + 1
        # freq[word] = freq[word] + 1
    return freq

def displayWordCount(listOfWords, freq):
    print('The Gettysburg Address contains', len(listOfWords), 'words.')
    print('The Gettysburg Address contains', len(freq), 'different words.')
    print()

def displayMostCommonWords(freq):
    print("The most common words and their frequencies are:")
    # listOfMostCommonWords = []
    # for word in freq:
    #     if freq[word] >= 6:
    #         listOfMostCommonWords.append((word, freq[word]))

    listOfMostCommonWords = \
    [(word, freq[word]) for word in freq if freq[word] >= 6]

    listOfMostCommonWords.sort(key=lambda x: x[1], reverse=True)
    for item in listOfMostCommonWords:
        print('    ', item[0] + ':', item[1])

main()

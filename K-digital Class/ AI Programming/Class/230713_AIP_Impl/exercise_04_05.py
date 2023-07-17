def main():
    word = getInput()

    if isTripleConsecutive(word.lower()):
        print('{} contains three successive letters in consecutive alphabetical order.'.format(word))
    else:
        print('{} does not contain three successive letters in consecutive alphabetical order.'.format(word))


def getInput():
    word = input("Enter a word: ")
    return word

def isTripleConsecutive(word):
    for i in range(len(word)-2):
        if word[i].isalpha() and ord(word[i])+1 == ord(word[i+1]) and ord(word[i+1])+1 == ord(word[i+2]):
            return True        
    return False


main()
def find_paindromes(word):
    if word == word[::-1]:
        return True
    else:
        return False

def main():
    word = list(input("write a word"))
    result = find_paindromes(word)
    print(result)

main()
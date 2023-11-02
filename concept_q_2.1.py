def isogram():
    i = input("Enter a word to check if it is an isogram: ")
    i = i.lower()
    letters = set()

    for letter in i:
        if letter.isalpha():
            if letter in letters:
                return False
            letters.add(letter)

    return True

iso_answer = isogram()
print(iso_answer)
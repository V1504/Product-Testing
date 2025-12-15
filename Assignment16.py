def CharacterChecker():
    char = input("Enter a character: ")
    if char.isalpha() and char.lower() not in 'aeiou':
        print(f"{char} is an alphabet.")
    else:
        print(f"{char} is Vowel.")
CharacterChecker()
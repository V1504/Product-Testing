word=input("Enter a word: ")
for i in range(0, len(word)):
    letter=word[i]
    print(f"{letter}:{word.count(letter)}")
def longest_word(sen):
    word=sen.split()
    longest=word[0]
    for w in word:
        if len(w)>len(longest):
            longest=w
            return longest
        sen=input("Enter a sentence: ")
        print("Longest word: ",longest_word())


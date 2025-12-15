def count_letters_digits(s):
    letters = 0
    digits = 0
    for ch in s:
        if ch.isalpha():
            letters+=1
        elif ch.isdigit():
            digits+=1
    return letters, digits
print(count_letters_digits("Infosys 123"))
print(count_letters_digits("ABCEFG"))
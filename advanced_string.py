def is_palindrome(text):
    cleaned_text=""
    for ch in text:
        if ch.isalnum():
            cleaned_text+=ch.lower()
            
    return cleaned_text==cleaned_text[::-1]
text="Madam, I'm Adam"
print(is_palindrome(text))
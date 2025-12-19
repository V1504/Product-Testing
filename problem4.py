def encrpt(s):
    words=s.split()
    encrypted=[]
    
    vowels="aeiouAEIOU"
    for i in range(len(words)):
        word=words[i]
        
        if i%2==0:
            encrypted.append(word[::-1])
        else:
            consonant=""
            vowel=""
            
            for ch in word:
                if ch in vowels:
                    vowel+=ch
                else:
                    consonants+=ch
            encrypted.append(consonants+vowel)
    return " ".join(encrypted)
print(encrpt("the sun rises in the east"))
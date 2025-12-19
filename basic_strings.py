def cnt(input_str):
    vowels="aeiouAEIOU"
    vowel_cnt=0
    consonant_cnt=0
    for ch in input_str.lower():
      if ch.isalpha():
          if ch in vowels:
              vowel_cnt+=1
          else:
              consonant_cnt+=1
        
    return vowel_cnt, consonant_cnt
input_str=input("Enter String: ")
vowels, consonant=cnt(input_str)
print(f"Vowels:{vowels},Consonanat: {consonant}")
        
def rev_words(s):
    words=s.split()
    reversed_words=[]
    
    for w in words:
        reversed_words.append(w[::-1])
        
    return " ".join(reversed_words)
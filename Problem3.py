def common_ch(s1,s2):
    res=""
    s1=s1.replace(" "," ")
    s2=s2.replace(" "," ")
    
    for ch in s1:
        if ch in s2 and ch not in res:
            res=res+ch
            
    if res=="":
        return -1
    else:
        return res
    
    sen1="I like Pyhton"
    sen2="Java is very popular language"
    print(common_ch(sen1,sen2))
def duplicates():
    dup=[]
    for num in lst:
        if lst.count(num)>1 and num not in dup:
            dup.append(num)
            return dup
    lst=list(map(int(input("Enter elements: ").split())))
    print("Duplicate elemets: ",duplicates(lst))
        
        
        
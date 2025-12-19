names=["Hat","Cat","Rabbit","Matter"]
count=0
count_at=0
for n in names:
        if len(n)==3 and n.endswith("at"):
            count_at+=1
            
            count_percent_at=0
            for n in names:
                count_percent_at+=1          
print("_at->",count_at)
print("%at%->",count_percent_at)

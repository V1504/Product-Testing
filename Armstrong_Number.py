num=int(input("Enter a number: "))
temp=num
total_sum=0
count=0
    
while temp>0:
        count+=1
        temp//=10
        
temp=num
while temp>0:
        digit=temp%10
        total_sum+=digit**count
        temp//=10
        
if num==total_sum:
        print(num,"is an Armstrong number")
else:
        print(num," is not an armstrong number")
        

        
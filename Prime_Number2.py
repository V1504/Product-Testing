def is_prime(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count=count+1   
            print(i,end=" ")
            if count==2:
                return True
            else:
                return False
            
number=int(input("Enter a number: "))
if is_prime(number):
    print(f"\n{number} is a prime number.")
else:
    print(f"\n{number} is not a prime number.")
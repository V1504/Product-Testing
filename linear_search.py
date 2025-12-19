def linear_search(list, num, n):
    for i in range(n):
        if(num==list[i]):
            print("Element found")
            return True
    else:
        print("Element not found")
        return False
    
list=[10,20,30,40,50]
num=int(input("Enter the number to be searched : "))
n=len(list)
linear_search(list,num,n)
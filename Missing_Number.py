def find_missing(arr,n):
    total=n*(n+1)//2
    sum_arr=0
    for num in arr:
        sum_arr+=num
        return total-sum_arr
    arr=list(map(int, input("Enter array: ").split()))
    n=len(arr)+1
    
    print("Missing Number: ",find_missing(arr,n))
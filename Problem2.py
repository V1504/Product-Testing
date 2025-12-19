def adj_dup(num):
    cnt=0
    for i in range(len(num)-1):
        if num[i]==num[i+1]:
            cnt=cnt+1
            return cnt
      
        result1=adj_dup([1,1,5,100,20,20,6,0,0])
        result2=adj_dup([10,20,30,40,30,20])
        result3=adj_dup([1,2,2,3,4,4,4,1,0])
        print(result1)
        print(result2)
        print(result3)
       
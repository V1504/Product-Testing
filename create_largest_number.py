def create_largest_number(num):
    num =[str(n) for n in num]
    num.sort(reverse=True)
    return "".join(num)
print(create_largest_number([23,45,67,12]))
  

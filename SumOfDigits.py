def sum_of_digits(number):
    sum= 0
    while number > 0:
        digit = number % 10
        sum =sum+ digit
        number=number/ 10
    return sum

num= int(input("Enter a number: "))
result= sum_of_digits(num)  
print("The sum of digits is:", result)
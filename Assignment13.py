def SumChecker():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if (num1%2==0 and num2%2==0):
       sum = num1 + num2
       print("Even Sum:", sum)
    elif (num1%2!=0 and num2%2!=0):
       product = num1 * num2
       print("Odd Product:", product)
    else:
       print("Mixed Numbers")
SumChecker()

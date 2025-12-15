def Calc():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    operation=input("Enter operation (+, -, *, /): ")
    if operation=='+':
        print(f"The sum is: {num1 + num2}") 
    elif operation=='-':
        print(f"The difference is: {num1 - num2}")
    elif operation=='*':
        print(f"The product is: {num1 * num2}")
    elif operation=='/':
        if num2 != 0:
            print(f"The quotient is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
Calc()
        
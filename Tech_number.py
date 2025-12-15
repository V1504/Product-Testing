def technum():
    num_str = input("Enter a number: ")

    if len(num_str) % 2 == 0:
        num = int(num_str)
        mid = len(num_str) // 2
        
        first_half = int(num_str[:mid])
        second_half = int(num_str[mid:])
        
        sum_val = first_half + second_half
        if (sum_val ** 2) == num:
            print(f"{num} is a Tech Number.")
        else:
            print(f"{num} is NOT a Tech Number.")
    else:
        print(f"{num_str} is NOT a Tech Number (must have an even number of digits).")

technum()
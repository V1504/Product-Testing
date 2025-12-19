def linearSearch():
    list = [23, 45, 67,89, 12, 34, 56, 78]
    item=int(input("Enter the item to be searched : "))
    found=False 
    for i in range (len(list)):
        if list[i]==item:
            found=True
            print(f"Item found at index {i}")
            break
        else:
            print("Item not found in the list")
            
linearSearch()
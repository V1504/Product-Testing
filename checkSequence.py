def checkSequence(num_list):
    for i in range(len(num_list)-2):
        if num_list[i] == 1 and num_list[i+1] == 2 and num_list[i+2] == 3:
            return True
    return False

print(checkSequence([1, 1, 2, 3, 1])) 


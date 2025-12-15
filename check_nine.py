def check_nime(num):
    return 9 in num[:4]
print(check_nime([1,2,9,3,4]))
print(check_nime([1,2,9]))
print(check_nime([1,2,3,4]))
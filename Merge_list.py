def merge_sort(lst1,lst2):
    merged=lst1+lst2
    merged.sort()
    return merged

lst1=list(map(int,input("Enter first list: ").split()))
lst2=list(map(int, input("Enter Second Lis: ").split()))
print("Merged List: ",merge_sort(lst1, lst2))
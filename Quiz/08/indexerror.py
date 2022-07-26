def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print("Oops!! The index is not exist in your list.")
    
list1 = [1,2,3,4]
print_list_element(list1, 4)
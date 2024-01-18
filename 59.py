# Write a python program to remove all the duplicates from a list

def remove_duplicates():
    user_list = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i']
    
    unique_list = list(set(user_list))
    print("List after removing duplicates:", unique_list)

remove_duplicates()

# Write a program that can create a new list from a given list where each item in the new list is square of the item of the old list

def new_list():
    user_list = [2, 4, 5, 7, 3, 9, 1]
    squared_list = [i ** 2 for i in user_list]
    print("Squared list:", squared_list)

new_list()

# Write a program to check if a list is in ascending order or not

def list_order_check():
    user_list = [2, 4, 5, 7, 3, 9, 1]
    new_list=sorted(user_list)
    if user_list==new_list:
        print("Your list is in ascending order")

    else:
        print("Opps! Your list is not in order")

list_order_check()
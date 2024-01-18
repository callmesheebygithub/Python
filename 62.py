# Write a python program to reverse a list

def reverse_list():
    user_list = [2, 4, 5, 7, 3, 9, 1]
    length = len(user_list)
    reversed_list = []

    for i in range(length - 1, -1, -1):
        reversed_list.append(user_list[i])

    print("Reversed list:", reversed_list)

reverse_list()

# Write a python program to find the max item from a list without using the max function

def find_max_value():
    user_list = [1, 2, 3, 4, 5, 6, 7, 5, 4, 77, 88, 90, 44, 33, 101]

    result = float('-inf')  # Initializing result to negative infinity

    for num in user_list:
        if num > result:
            result = num

    print("Maximum value in the list:", result)

find_max_value()
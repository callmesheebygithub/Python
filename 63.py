# Write a python program to search a given number from a list

def search_list():
    user_list = [2, 4, 5, 7, 3, 9, 1]
    search = int(input("Enter the number to search in the list: "))
    found = False

    for index, value in enumerate(user_list):
        if search == value:
            print(f"Value {search} found at index {index}.")
            found = True
            break

    if not found:
        print("Value not found in the list.")

search_list()

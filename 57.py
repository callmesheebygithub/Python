# Write a program which can remove a particular character from a string. 

def remove():
    user_input=str(input("Enter your Text: "))
    rem_char=str(input("Which character do you want to remove: "))

    user_input=user_input.replace(rem_char,"")

    print(user_input)

remove()
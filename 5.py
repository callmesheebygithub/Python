# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

def reverse():
    user_input=str(input("Enter Four Digit Number: "))
    length=len(user_input)
    if length <=4:
        user_input=user_input[::-1]
        return user_input

    else:
        print("Your Given input is not matching our conditions. Please try again!")

        
    
Obj=reverse()
print(Obj)

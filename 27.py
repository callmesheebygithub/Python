# Write a program that can find the factorial of a given number provided by the user.

def factorial():
    user_inp=int(input("Enter the Number: "))
    
    if user_inp<0:
        return "Factorial is not defined for negative numbers."

    elif user_inp == 0 or user_inp==1:
        return 1
    else:
        factorial=user_inp*(user_inp-1)

    return factorial

Obj=factorial()
print(Obj)
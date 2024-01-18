# Write  a program that will tell whether the given number is divisible by 3 & 6.

def division_checker():
    
    user_inp=int(input("Enter Number: "))

    if user_inp % 3==0 and user_inp% 6==0:
        print("Number is divisble by both 3 and 6")

    elif user_inp % 3==0 :
        print("Number is divisble by 3")

    elif user_inp% 6==0:
        print("Number is divisble by 6")

    else :
        print("Number isn't divisble by 3 or 6")

division_checker()
# Write a program that will tell whether the given year is a leap year or not.

def leap_year():
    user_inp=int(input("Enter your year for checking leap year: "))
    if user_inp% 4==0:
        print("It's a Leap Year: ",user_inp)

    else:
        print("It's not a leap year")

leap_year()
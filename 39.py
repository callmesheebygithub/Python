# Take a number from the user and find the number of digits in it. 

def number_counts():
    user_inp = int(input("Enter Number: "))
    digit = str(user_inp)
    count = 0
    for i in digit:
        count += 1

    return count

count_of_digits = number_counts()
print(f"The number of digits in the given number is: {count_of_digits}")

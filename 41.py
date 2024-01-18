# Find the reverse of a number provided by the user(any number of digit) 

def reverse_digit():
    user_inp = int(input("Enter Number: "))
    reverse = 0

    if user_inp >= 0:
        reverse = int(str(user_inp)[::-1])
    else:
        reverse = int(str(abs(user_inp))[::-1])

    print(f"The reverse of the number is: {reverse}")

reverse_digit()

def reverse_digit():
    user_inp = int(input("Enter Number: "))
    reverse = 0

    while user_inp != 0:
        remainder = user_inp % 10
        reverse = reverse * 10 + remainder
        user_inp //= 10

    print(f"The reverse of the number is: {reverse}")

# reverse_digit()

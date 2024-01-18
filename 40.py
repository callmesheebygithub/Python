# Print all factors of a given number provided by the user.

def factor():
    user_inp = int(input("Enter the Number: "))
    for i in range(1, user_inp + 1):
        if user_inp % i == 0:
            print(i, end=" ")

factor()

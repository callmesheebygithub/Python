# Write a program that can multiply 2 numbers provided by the user without using the * operator

def multiplication():
    number = int(input("Enter Number: "))
    mul_number = int(input("Enter Multiplication Number: "))
    result = 0
    for i in range(mul_number):
        result = result + number

    return result

result = multiplication()
print(result)

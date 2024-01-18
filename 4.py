#4. Write a program that will give you the sum of 3 digits

def sum():
    user_input=int(input("Enter Number: "))

    a=user_input % 10 #(345 % 10 = 5)
    user_input=user_input // 10 # (345 // 10 = 34)
    b= user_input %10 #(34 % 10 = 4)
    c= user_input // 10 #(34 // 10 =3)

    addition = a+b+c
    return addition

Obj=sum()
print(Obj)
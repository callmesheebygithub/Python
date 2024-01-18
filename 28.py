# Write a program to print the first 25 odd numbers

def odd_sum():
    user_inp=int(input("Enter Number: "))

    result=0

    for i in range(0,user_inp+1):
        if i %2==0:
            continue
        else:
            result=result+i

    return result

# obj=odd_sum()
# print(obj)

def odd_print():
    user_inp=int(input("Enter Number: "))

    for i in range(0,user_inp+1):
        if i %2==0:
            continue
        else:
            print(i,end=" ")

odd_print()

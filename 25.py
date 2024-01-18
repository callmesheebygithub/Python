# Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

def sum_of_n():
    user_inp=int(input("Enter Number: "))
    addition=0
    for i in range(0,user_inp+1):
        addition=addition+i 
    return addition

Obj=sum_of_n()
print(Obj)
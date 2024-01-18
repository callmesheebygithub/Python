# User will input (2numbers).Write a program to swap the numbers

def number_swap():
    var1=input("Enter First value: ")
    var2=input("Enter Second value: ")
    var3=var1
    var1=var2
    return var1 , var3
        
var1,var2=number_swap()

print("Here's your swapping result: ",var1," ",var2)


def number_swap():
    var1=int(input("Enter First value: "))
    var2=int(input("Enter Second value: "))

    var1=var1+var2 
    var2=var1-var2
    var1=var1-var2

    return var1,var2

var1,var2=number_swap()
print("Here's your swapping result: ",var1," ",var2)
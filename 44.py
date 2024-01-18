# Write  a program to print the following pattern
#         *
#       * * *
#     * * * * *
#    * * * * * * *
# * * * * * * * * *

def triangle_pattern():
    user_inp=int(input("Enter number to draw triangle: "))

    for i in range(0,user_inp):
        if i % 2==0:
            continue
        else:
            for j in range(i):
                print("*",end=" ")
        print("\n")

# triangle_pattern()
        
def triangle_pattern():
    user_inp = int(input("Enter the number of rows for the triangle: "))

    for i in range(user_inp):
        for j in range(user_inp - i - 1):
            print(" ", end=" ")

        for k in range(2 * i + 1):
            print("*", end=" ")

        print()

triangle_pattern()

# Write a program to print the following pattern
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

def number_pattern():
    rows = int(input("Enter the number of rows for the pattern: "))

    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(j, end=" ")

        for k in range(i-1,0,-1):
            print(k,end=" ")

        print()

number_pattern()

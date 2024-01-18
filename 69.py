# Write a program to merge 2 list without using the + operator

def list_merge():
    odd_list=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    even_list=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    for i in odd_list:
        even_list.append(i)

    print("Merge List",even_list)

list_merge()



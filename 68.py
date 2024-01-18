# Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list and the 2nd one will contain all the even numbers 

def dif_list():
    user_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    odd_list=[]
    even_list=[]
    for i in user_list:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(f"here is your odd list{odd_list}")
    print(f"here is your even list{even_list}")

dif_list()
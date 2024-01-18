# Closest Number
def closest_number(array,close_num):
    flag=False
    array=array
    clos_num=close_num
    array.sort()
    index=-1
    length=len(array)-1  
    for i in array:
        index=index+1
        if i==clos_num:
            flag=True
            break
    if flag==False: 
        print("Number Doesn't exist in the given list please try another number")
    else:
        if index>=length:
            print('1st Closest Number is:',array[index-1],'\n2nd Closest Number is:',array[index+0])
        elif index<=0:
            print('1st Closest Number is:',array[index-0],'\n2nd Closest Number is:',array[index+1])
        else:
            print('1st Closest Number is:',array[index-1],'\n2nd Closest Number is:',array[index+1])
##array=[5,7,3,2,9,0,11,14,1,12,18,19]
##close_num=int(input("Enter Number: "))
##closest_number(array,close_num)
##n = int(input())
import random
a=random.random()
print(a)

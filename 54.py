# Count the frequency of a particular character in a provided string. Eg 'hello how are you' is the string, the frequency of h in this string is 2.

def frequency():
    dict={}
    user_inp=str(input("Enter your Text: "))

    for i in user_inp:
        if i in dict:
            dict[i]+=1

        else:
            dict[i]=1

    print (dict)

frequency() 
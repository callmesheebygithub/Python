# Count the number of vowels in a string provided by the user.

def vowels_count():
    vowels=['a','e','i','o','u','A','E','I','O','U']
    user_inp=str(input("Enter your Text: "))
    count=0
    for i in user_inp:
        if i in vowels:
            count+=1

    print(count)

vowels_count()
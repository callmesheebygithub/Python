# User will input (3ages).Find the oldest one

def old_age():
    l=[]
    for i in range(3):
        user_input=float(input(f"Enter Person {i+1} Age: "))
        l.append(user_input)
    for j in l:
        oldest=l[0]
        if j>oldest:
            oldest=j
    return oldest

Obj=old_age()
print("Here is Oldest One: ",Obj)

# 2nd Method

def old_age():
    l=[]
    for i in range(3):
        user_input=float(input(f"Enter Person {i+1} Age: "))
        l.append(user_input)

    return max(l)

OBJ=old_age()
print(OBJ)
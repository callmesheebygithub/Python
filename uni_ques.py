##Given the participants' score sheet for your University Sports Day, you are
##required to find the runner-up score. You are given n scores. Store them in a
##list and find the score of the runner-up.

##Input Format
##
##The first line contains n. The second line contains an array A[]  of n
##integers each separated by a space.

n = int(input())
arr = list(map(int, input().split()))
A=[]
if (n>=2 and n<=10):
    for i in arr:
        if (i>=-100 and i<=100):
            A.append(i)
A.sort()
##print(A)
final=[]
for j in A:
##    print(j)
    if j not in final:
        final.append(j)
final.sort()
print(final[-2])

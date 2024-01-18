# How to find the duplicate number on a given integer array?
a = array.array('i', range(1, 100,2))
c=[i for i in range(0,100)]
l=[]
for i in a:
    for j in c:
      if i==j:
          l.append(i)
          break
print("Duplicated array: ",l)
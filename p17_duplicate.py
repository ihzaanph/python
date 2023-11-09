n=input("Enter the list elements seperated by comma:")
n=n.split(',')
dup=[]
new=[]
for i in n:
    if i not in new:
        new.append(i)
    else:
        dup.append(i)
print("Elements after removing duplicate :\n",new)
print('Duplicate elements are :\n',dup)

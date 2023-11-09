a=input("Enter a list of colors : ")
color=list(a.split(','))
l=len(color)
print("List of colors are : ",color)
print("Alternative colors : ",color[0:l:2])



l1=set(input("enter the colour 1").split())
l2=set(input("enter the colour 2").split())
print("color is in 1st but not in 2nd are:",{i for i in l1-l2})

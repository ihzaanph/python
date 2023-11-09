a=input("enter the word")
b=a.lower()
s=b+"ing"
z=b+"ly"
if(b[-3:]=="ing"):
    print(z)
else:
    print(s)

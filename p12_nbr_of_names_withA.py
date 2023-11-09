c=0
a=input("Enter the nameds : ")
name=list(a.split(','))
for i in name :
    if(i[0][0]=="a" or i[0][0]=="A"):
      c=c+1
print("Number of name with A : ",c)

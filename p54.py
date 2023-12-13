inf=False
try:
    inf=open('abc.txt','r')
    lines=inf.readlines()
    inf.close()
    lineText=input('Enter the String to be deleted :')
    inf=open('abc.txt','w')
    for line in lines:
        if line.strip()!=lineText:
            inf.write(line)
    print("Deleted Successfully")
except IOError as e:
    print(e)  
finally:
     if inf:inf.close()
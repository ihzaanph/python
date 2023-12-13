inf=False
try:
    with open('abc.txt','r') as inf:
     lines=inf.readlines()
    print('Number of Lines in the File = ',len(lines))
except IOError as e:
   print(e)
finally:
   if inf:inf.close()
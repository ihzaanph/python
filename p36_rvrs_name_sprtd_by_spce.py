def rname(name):
    for word in name[::-1]:
      print(word,end=" ")
n= input("Enter a name").split()
rname(n)

word=input("enter the word")
letters={}
for l in word:
    letters[l]=letters.get(l,0)+1
print(letters)
       

list=input('Enter a list of words ' )
word=list.split()
num=int(input('Enter a Number : '))
word=[i for i in word if (len(i)>num)]
print("Words that are longer than ",num," are ",word)
    

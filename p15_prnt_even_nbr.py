a=input("Enter numbers seperated by comma:")
a=list(map(int,a.split(',')))
result=[item for item in a if item%2==0]
print("Even numbers are : ",result)

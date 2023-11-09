print('Q:A')
a=input("Enter numbers seperated by comma:")
a=list(map(int,a.split(',')))
print("List of positive numbers:")
pos=[item for item in a if item>0]
print(pos)
print('Q:B')
a=input("Enter numbers seperated by comma:")
a=list(map(int,a.split(',')))
sqr=[item**2 for item in a]
print("Square of list elements:",sqr)
print('Q:C')
v1=['a','A','e','E','i','I','o','O','u','U']
s=input('Enter a string:')
n=list(s)
v=[item for item in n if item in v1]
print('Vowels:',v)
print('Q:D')
a=input("Enter numbers seperated by comma:")
a=list(map(int,a.split(',')))
p=[item for item in a if item%2==1]
print("List with out even numbers=",p)
print('Q:E')
n=int(input("Enter the year limit:"))
p=[year for year in range(2023,n) if year%4==0 and year%100!=0 or year%400==0]
print('Leap years are:',p)
        

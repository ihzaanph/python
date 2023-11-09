def even(num):
    for i in num:
        if(i==237):
            break
        elif not i%2:
            print(i)
n=input("enter the number")
n=list(map(int,n.split()))
print("even numbers are")
even(n)
       

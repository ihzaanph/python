import math
square = lambda side: side**2
rectangle = lambda length, breadth: length * breadth
triangle= lambda a, b, c: math.sqrt((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))
side=int(input('Enter the side of a square'))
print('Area of square',square(side))
length=int(input('Enter the length of the rectangle'))
breadth=int(input('Enter the breadth of the rectangle'))
print('Area of rectangle', rectangle (length,breadth))
a=int(input('Enter first side'))
b=int(input('Enter second side'))
c=int(input('Enter third side'))
print('Area of triangle', triangle (a,b,c))

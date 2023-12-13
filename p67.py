class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()

r1 = Rectangle(5, 10)
r2 = Rectangle(3, 8)

if r1 < r2:
    print("Rectangle 1 has a smaller area than Rectangle 2")
else:
    print("Rectangle 2 has a smaller area than Rectangle 1")
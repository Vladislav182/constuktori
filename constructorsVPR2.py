class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return self.height + self.width
rectangle = Rectangle(10, 2)
print(f"Liceto e {rectangle.area()}")
print(f"Perimetura e {rectangle.perimeter()}")

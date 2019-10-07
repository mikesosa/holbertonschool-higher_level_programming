#!/usr/bin/python3
class Rectangle:
    """
        Class that defines a Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integeri")
            return
        if value < 0:
            raise ValueError("width must be >= 0")
            return
        self.__width = value

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integeri")
            return
        if value < 0:
            raise ValueError("width must be >= 0")
            return
        self.__height = value

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        perimeter = self.__width + self.__height + self.__width + self.__height
        return perimeter

    def __str__(self):
        new_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                new_str = new_str + str(self.print_symbol)
            if i < (self.__height - 1):
                new_str = new_str + "\n"
        return new_str

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        x, y = size, size
        return cls(x, y)

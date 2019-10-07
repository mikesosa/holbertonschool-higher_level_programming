#!/usr/lib/python3
class Rectangle:
    """
        Class that defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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

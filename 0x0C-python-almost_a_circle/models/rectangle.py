#!/usr/bin/python3
"""Containf class rectangle"""

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializers"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter, and validation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter, and validation"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter, and validation"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter, and validation"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area"""
        return self.__width * self.__height

    def display(self):
        """Prints to stdout the recatangle with '#' char"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.width + self.x):
                if x >= self.x:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()

    def __str__(self):
        """Returns a description of the rectangle"""
        return "[Rectangle] ({}) {}/{}\
 - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updating rectangle"""
        if args is not None and len(args):
            for i, value in enumerate(args):
                if i is 0:
                    self.id = value
                elif i is 1:
                    self.width = value
                elif i is 2:
                    self.height = value
                elif i is 3:
                    self.x = value
                elif i is 4:
                    self.y = value
                else:
                    raise Exception("Too many arguments")
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                elif key == "width":
                    self.width = kwargs["width"]
                elif key == "height":
                    self.height = kwargs["height"]
                elif key == "x":
                    self.x = kwargs["x"]
                elif key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns a description on a dict"""
        my_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return my_dict

#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a description of the square"""
        return "[Square] ({}) {}/{}\
 - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ size setter, and validation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value\


    def update(self, *args, **kwargs):
        """Update square method"""
        if args is not None and len(args):
            for i, value in enumerate(args):
                if i is 0:
                    self.id = value
                elif i is 1:
                    self.size = value
                elif i is 2:
                    self.x = value
                elif i is 3:
                    self.y = value
                else:
                    raise Exception("Too many arguments")
        else:
            for i in kwargs:
                if i is "size":
                    self.size = kwargs["size"]
                elif i is "x":
                    self.x = kwargs["x"]
                elif i is "y":
                    self.y = kwargs["y"]
                elif i is "id":
                    self.id = kwargs["id"]

    def to_dictionary(self):
        """Returns a description on a dict"""
        my_dict = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return my_dict

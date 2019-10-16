#!/usr/bin/python3
""" Module has class BaseGeometry """


class BaseGeometry:
    """I'll be 30 next year :v"""

    def area(self):
        """Raises error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Cheks if value is integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greather than 0".format(name))

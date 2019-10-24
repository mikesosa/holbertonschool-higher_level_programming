#!/usr/bin/python3
""" module and base of all other classes """

import json
import turtle
import time

class Base():
    """ BaseClass of all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiator """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON of a dictionary """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string to a file """
        temp = []
        if list_objs is None or len(list_objs) is 0:
            pass
        else:
            for i in list_objs:
                temp.append(cls.to_dictionary(i))
        x = cls.to_json_string(temp)
        with open("{}.json".format(cls.__name__),
                  mode='w', encoding='utf-8') as f:
            f.write(x)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of a json string """
        if json_string is None or len(json_string) is 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes of the dict """
        if cls.__name__ == "Rectangle":
            temp = cls(width=6, height=9)
        if cls.__name__ == "Square":
            temp = cls(size=69)
        temp.update(**dictionary)

        return temp

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        temp = []
        try:
            with open("{}.json".format(
                    cls.__name__), "r", encoding='utf-8') as f:
                temp2 = cls.from_json_string(f.read())
        except:
            return []
        for i in temp2:
            temp.append(cls.create(**i))
        return temp

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ lol i didnt do dis """
        pass

    @classmethod
    def load_from_file_csv(cls):
        """ I dont like unit tests"""
        pass

    @staticmethod
    def createRectangle(i, shape):
        shape.forward(i.width)
        shape.right(90)
        shape.forward(i.height)
        shape.right(90)
        shape.forward(i.width)
        shape.right(90)
        shape.forward(i.height)
        shape.right(90)

    @staticmethod
    def createSquare(i, shape):
        shape.forward(i.size)
        shape.right(90)
        shape.forward(i.size)
        shape.right(90)
        shape.forward(i.size)
        shape.right(90)
        shape.forward(i.size)
        shape.right(90)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ i got too much other stuff to do. """
        yPosition = 250
        xPosition = -300
        shape = turtle.Turtle()
        shape.up()
        shape.color("blue")

        for i in list_rectangles:
            shape.begin_fill()
            shape.goto(xPosition, yPosition)
            Base.createRectangle(i, shape)
            shape.end_fill()
            time.sleep(1)
            xPosition = xPosition + i.width + 10

        yPosition = 100
        xPosition = -300

        for i in list_squares:
            shape.begin_fill()
            shape.goto(xPosition, yPosition)
            Base.createSquare(i, shape)
            shape.end_fill()
            time.sleep(1)
            xPosition = xPosition + i.size + 10

        shape.done()

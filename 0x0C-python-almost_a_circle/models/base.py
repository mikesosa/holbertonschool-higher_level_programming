#!/usr/bin/python3
import json


class Base:

    _nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ls = []
        if list_objs is None or not len(list_objs):
            pass
        else:
            for i in list_objs:
                ls.append(cls.to_dictionary(i))
        x = cls.to_json_string(ls)
        with open("{}.json".format(cls.__name__),
                  mode="w", encoding="utf-8") as f:
            f.write(x)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not len(json_string):
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dum = cls(width=6, height=9)
        if cls.__name__ == "Square":
            dum = cls(size=69)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        ls = []
        try:
            with open("{}.json".format(cls.__name__),
                      mode="r", encoding='utf-8') as f:
                temp = cls.from_json_string(f.read())
        except:
            return []
        for i in temp:
            ls.append(cls.create(**i))
        return ls

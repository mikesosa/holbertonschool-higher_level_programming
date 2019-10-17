#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns class to a dictionaty"""
        if attrs is None:
            return self.__dict__
        dic = {}
        for item in attrs:
            if item is "first_name":
                dic[item] = self.first_name
            elif item is "last_name":
                dic[item] = self.last_name
            elif item is "age":
                dic[item] = self.age
        return dic

    def reload_from_json(self, json):
        """Replacing values of a class from dict"""
        for item in json:
            if item is "first_name":
                self.first_name = json.get("first_name")
            elif item is "last_name":
                self.last_name = json.get("last_na,e")
            elif item is "age":
                self.age = json.get("age")

#!/usr/bin/python3
""" modul  base """
import json


class Base:
    """ doc """
    __nb_objects = 0

    def __init__(self, id=None):
        """ func doc """
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ doc function """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ doc function """
        filename = cls.__name__+".json"
        with open(filename, 'w', encoding="utf-8") as f:
            list = []
            if list_objs is None or len(list_objs) == 0:
                json.dump(json.loads(cls.to_json_string(list)), f)
            else:
                for ele in list_objs:
                    list.append(ele.to_dictionary())
                json.dump(json.loads(cls.to_json_string(list)), f)

    @staticmethod
    def from_json_string(json_string):
        """ doc function """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ doc function """
        if cls.__name__ == "Sqare":
            dummy = cls(1)
        if cls.__name__ == "Rectngle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ doc function """
        filename = cls.__name__+".json"
        try:
            with open(filename, encoding="utf-8") as f:
                newlist = []
                dict = cls.from_json_string(json.dumps(json.load(f)))
                for ele in dict:
                    newlist.append(cls.create(**ele))
                return newlist
        except FileNotFoundError:
            return []

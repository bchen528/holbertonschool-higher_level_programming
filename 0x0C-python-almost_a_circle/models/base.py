#!/usr/bin/python3
import json
"""JavaScript Object Notation"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instance attributes
        Args:
            id (int): id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation of list_dictionaries
        Args:
            list_dictionaries (obj): object
        Returns:
            JSON string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            cls (cls): class
            list_objs (file): list of instances who inherits of Base
        """
        filename = "{:s}.json".format(cls.__name__)

        content = []
        for i in range(len(list_objs)):
            content.append(cls.to_dictionary(list_objs[i]))

        with open(filename, mode="w", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string (str): string representing a list of dictionaries
        Returns:
            list of json string
        """
        a_list = []
        if json_string is not None and json_string != "":
            a_list = json.loads(json_string)
        return a_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary
        Returns:
            an instance with all attributes already set
        """
        dummy = cls(1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Returns:
            list of instances
        """
        filename = "{:s}.json".format(cls.__name__)

        try:
            with open(filename, mode="r", encoding="utf-8") as a_file:
                content_string = a_file.read()  # str of list of dictionaries
            a_list = cls.from_json_string(content_string)  # str to list
            list_instances = []
            for i in range(len(a_list)):  # a_list[i]: dictionary of attributes
                list_instances.append(cls.create(**a_list[i]))
        except:
            list_instances = []

        return list_instances

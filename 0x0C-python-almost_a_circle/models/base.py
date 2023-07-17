#!/usr/bin/python3
""" Base """
import json, csv

class Base:
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"

        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise TypeError(f"Unsupported class: {cls.__name__}")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                return [cls.create(**obj_dict) for obj_dict in data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and saves instances to a CSV file"""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            else:
                raise TypeError(f"Unsupported class: {cls.__name__}")
            writer.writerow(fieldnames)
            for obj in list_objs:
                row = [getattr(obj, field) for field in fieldnames]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes and loads instances from a CSV file"""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader)

                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fieldnames = ['id', 'size', 'x', 'y']
                else:
                    raise TypeError(f"Unsupported class: {cls.__name__}")

                obj_list = []

                for row in reader:
                    obj_dict = {field: int(value) for field, value in zip(fieldnames, row)}
                    obj_list.append(cls.create(**obj_dict))

                return obj_list
        except FileNotFoundError:
            return []

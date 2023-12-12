#!/usr/bin/python3
""" base.py """
import json
import csv
import turtle
import random


class Base:
    """base of all classes: 'id' manager to avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ('[]')
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representatio to a file"""
        dlist = []
        if list_objs is not None:
            for item in list_objs:
                dlist.append(item.to_dictionary())
        dlist = cls.to_json_string(dlist)
        with open(f'{cls.__name__}.json', 'w+', encoding='utf-8') as file:
            file.write(dlist)

    @staticmethod
    def from_json_string(json_string):
        """Returns: list of JSON string representation 'json_string'"""
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns: an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns: a list of instances"""
        objlist = []
        try:
            with open(f'{cls.__name__}.json', 'r', encoding='utf-8') as file:
                dlist = cls.from_json_string(file.read())
                [objlist.append(cls.create(**d)) for d in dlist]
        except FileNotFoundError:
            pass
        return (objlist)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        with open(f'{cls.__name__}.csv', 'w+', encoding='utf-8') as csvf:
            spamwriter = csv.writer(csvf)
            for obj in list_objs:
                spamwriter.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        objlist = []
        try:
            with open(f'{cls.__name__}.csv', 'r', encoding='utf-8') as csvf:
                spamreader = csv.reader(csvf)
                for s in spamreader:
                    obj = cls(1, 1)
                    d = obj.to_dictionary()
                    for i in range(len(s)):
                        d[list(d)[i]] = int(s[i])
                    obj.update(**d)
                    objlist.append(obj)
        except FileNotFoundError:
            pass
        return (objlist)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window & draws all the Rectangles & Squares"""
        turtle.bgcolor('black')
        # screen
        screen = turtle.Screen()
        screen.setworldcoordinates(0, 0, 200, 200)
        # turtle
        donatello = turtle.Turtle(visible=False)
        donatello.speed('fastest')
        # axis
        distance, tick = 200, 10
        donatello.pencolor('white')
        donatello.dot()
        for i in range(2):
            for _ in range(-1 * distance // 2, distance // 2, tick):
                donatello.forward(tick)
                donatello.dot()
            donatello.goto(0, 0)
            donatello.setheading(90)
        # draw rectangles & squares
        dim = ['width', 'height']
        colors = ['red', 'purple', 'orange', 'yellow',
                  'green', 'blue', 'magenta', 'white']
        for rec in list_rectangles + list_squares:
            recd = rec.to_dictionary()
            donatello.penup()
            donatello.goto(recd['x'], recd['y'])
            donatello.pendown()
            donatello.pencolor(random.choice(colors))
            for i in range(4):
                donatello.dot()
                donatello.setheading(90 * i)
                cote = 'size' if rec.__class__.__name__ == 'Square' \
                    else dim[i % 2]
                donatello.forward(recd[cote])
        # keep the window open
        turtle.done()

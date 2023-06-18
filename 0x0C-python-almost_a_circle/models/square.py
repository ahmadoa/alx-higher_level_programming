#!/usr/bin/python3
"""defining class Square Inheriting from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square Instance
        Args:
            size: size of square
            x: position x
            y: position y
            id: square id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding __str__ method from super class"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """read args and assign the values to attributes accordingly"""
        attr = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                    args + attr[len(args):len(attr)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of Square class"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

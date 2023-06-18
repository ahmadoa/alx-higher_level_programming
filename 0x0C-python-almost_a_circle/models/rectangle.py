#!/usr/bin/python3
"""defining subClass Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """SubClass rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle subclass instance
        Args:
            width: width of rectangle
            height: height of rectangle
            x: position x
            y: position y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of rect getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width of rect setter"""
        if type(width) != int:
            raise TypeError("{} must be an integer".format(width))
        if width <= 0:
            raise ValueError("{} must be > 0".format(width))
        self.__width = width

    @property
    def height(self):
        """height of rect getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height of rect setter"""
        if type(height) != int:
            raise TypeError("{} must be an integer".format(height))
        if height <= 0:
            raise ValueError("{} must be > 0".format(height))
        self.__height = height

    @property
    def x(self):
        """position x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """position x setter"""
        if x < 0:
            raise ValueError("{} must be >= 0".format(x))
        self.__x = x

    @property
    def y(self):
        """position y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """position y setter"""
        if y < 0:
            raise ValueError("{} must be >= 0".format(y))
        self.__y = y

    def area(self):
        """ calculates the area surface of thr rectangole"""
        return self.__width * self.__height

    def display(self):
        """prints a representation of rect using #"""
        for posy in range(self.x):
            print()
        for h in range(self.height):
            for posx in range(self):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the og __str__ method"""
        return "[Rectangle] ({}) {}/{} {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """retrieve all args and assign each accordingly"""
        attr = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y = \
                    args + attr[len(args):len(attr)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of the Rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}

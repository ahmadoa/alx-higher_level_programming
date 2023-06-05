"""Defining class Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes new rectangle
        Args:
            width (int): width value of rectangle
            height (int): height value of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width value of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new value of width
        Args:
            value (int): new value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height value of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets new height value
        Args:
            value (int): new value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2 + self.__height * 2)

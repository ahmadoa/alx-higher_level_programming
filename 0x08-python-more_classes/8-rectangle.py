#!/usr/bin/python3
"""defining rectangle class"""


class Rectangle:
    """class Rectangle

    Attributes:
        number_of_instances (int): number of instances
        print_symbol (any): symbol for string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes new rectangle
        Args:
            width (int): value of width
            height (int): height value of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """returns width value of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new width value
        Args:
            value (int): new width value
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
            value (int): new height value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle's area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """returns printable representation of rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        printable = []
        for i in range(self.__height):
            for j in range(self.__width):
                printable.append(str(self.print_symbol))
            if i != self.__height - 1:
                printable.append("\n")
        return ("".join(printable))

    def __repr__(self):
        """returns string representation of rectangle"""
        pr = "Rectangle(" + str(self.__width)
        pr += ", " + str(self.__height) + ")"
        return pr

    def __del__(self):
        """returned when an instance of rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns rectangle instance with the greater area
        Args:
            rect_1 (Rectangle): first rectangle instance
            rect_2 (Rectangle): second rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_rect_1 = rect_1.area()
        area_rect_2 = rect_2.area()
        if area_rect_1 >= area_rect_2:
            return rect_1
        return rect_2

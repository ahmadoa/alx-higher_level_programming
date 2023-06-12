#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """ MyInt inherits from int & reverses behaviour of != & == """
    def __eq__(self, other):
        """ == inverts to != """
        return super().__ne__(other)

    def __ne__(self, other):
        """ != inverts to == """
        return super().__eq__(other)

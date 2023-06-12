#!/usr/bin/python3
"""defining class MyList that inherits from list class"""


class MyList(list):
    """represents MyList """
    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))

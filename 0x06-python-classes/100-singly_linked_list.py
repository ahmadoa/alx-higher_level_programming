#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): data of new Node.
            next_node (Node): the new node of the new Node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """gets val of data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter of data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets val of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets new value to next_value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Initialize SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node to singlyLinkedList.

        Args:
            value (Node): node to add
        """
        new_node = Node(value)
        if new_node.next_node = None:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """printable representation of the class"""
        elements = []
        temp = self.__head
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(elements))

#!/usr/bin/python3
"""
Singly linked list Module
"""


class Node:

    """
    Node class
    Attributes:
        data (int): the data stored in the node
        next_node (Node): a pointer to the next node
        in the linked list

    """
    def __init__(self, data, next_node=None):

        """
        Class initializer

        Args:
            data (int): the data stored in the node.
            next_node (Node): a pointer to the next node

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter of the attribute data

        Returns:
            data: the stored data

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter of the attribure data

        Args:
            value (int): the given data

        Raises:
            TypeError: if value is not integer

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter of the next_node

        Returns:
            next_node: a pointer to the next node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter of the next_node

        Args:
            value (Node): a pointer to the next node

        Raises:
            TypeError: if value not node or None

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    SiglyLinkedList defines the singly linked list

    Attributes:
        head (Node): a pointer to the singly linked list

    """
    def __init__(self):
        """
        Class initializer
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts new Node into the correct soeted position
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        result = []
        tmp = self.__head
        while tmp is not None:
            result.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(result)

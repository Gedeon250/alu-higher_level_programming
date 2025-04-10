#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initiation of a new Rectangle
        :param width: The width of the initiated rectangle
        :type width: int
        :param height: The height of the initiated rectangle
        :type height: int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect


# Comment here

# my_rectangle = Rectangle(2, 4)
# print(str(my_rectangle))
# print("--")
# print(my_rectangle)
# print("--")
# print(repr(my_rectangle))
# print("--")
# print(hex(id(my_rectangle)))
# print("--")

# Create new instance based on representation
# new_rectangle = eval(repr(my_rectangle))
# print(str(new_rectangle))
# print("--")
# print(new_rectangle)
# print("--")
# print(repr(new_rectangle))
# print("--")
# print(hex(id(new_rectangle)))
# print("--")

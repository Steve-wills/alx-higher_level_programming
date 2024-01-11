#!/usr/bin/python3

"""A module that defines a Rectangle Class"""


class Rectangle:
    """A rectangle class with height and width"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """A method that instantiates private attributes"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError('height must be >= 0')
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):

            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of a square"""
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        """Returns the perimeter of a rectangle"""
        return 2 * (self.height + self.width)

    def __str__(self):
        """Returns a '#' symbol"""
        final = ""
        if (self.width == 0 or self.height == 0):
            return (final)
        for i in range(self.height):
            for j in range(self.width):
                final = final + str(self.print_symbol)
            if i != (self.height - 1):
                final = final + "\n"
        return (final)

    def __repr__(self):
        """Returns a string to create another class"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        Rectangle.width = Rectangle.height = size
        return (Rectangle(size, size))

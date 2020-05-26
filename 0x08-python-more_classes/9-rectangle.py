#!/usr/bin/python3
"""
A Rectangle
"""


class Rectangle:
    """
    functions and data
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instatiation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """hsajwushw"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            for a in range(self.__height):
                if a == self.__height - 1:
                    string += self.__width * str(self.print_symbol)
                else:
                    string += self.__width * str(self.print_symbol) + '\n'
            return string

    def __repr__(self):
        """Returns a representation of printable string"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Destructors are called when an object gets destroyed """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ rect_1 and rect_2 must be instance of rectangle class """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance
        """
        height = size
        width = size
        return cls(height, width)

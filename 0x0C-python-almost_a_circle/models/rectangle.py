from models.base import Base
""" Rectangle """


class Rectangle(Base):
    """Defines a Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width of a rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle instance"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle instance"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves x coordinate of a rectangle instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x coordinate of a rectangle instance"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves y coordinate of a rectangle instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y coordinate of a rectangle instance"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of a rectangle instance"""
        return self.width * self.height

    def display(self):
        "Prints in stdout the Rectangle instance with the character #"
        if self.__width == 0 or self.__height == 0:
            return ""

        display_rectangle = ""
        for _ in range(self.__y):
            display_rectangle += "\n"

        for _ in range(self.__height):
            display_rectangle += " " * self.__x + "#" * self.__width + "\n"

        print(display_rectangle.rstrip())

    def __str__(self):
        """Returns a string representation"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} "
            f"- {self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        "Assigns an argument to each attribute"
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle instance"""
        return {
            'id': self.__id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

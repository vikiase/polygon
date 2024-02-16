import math


class Rectangle:
    def __init__(self, width, height, side_length=0):
        self.width = width
        self.height = height
        self.side_length = side_length

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width
        return self.width

    def set_height(self, new_height):
        self.height = new_height
        return self.height

    def get_area(self):
        result = self.width * self.height
        return result

    def get_perimeter(self):
        result = (2 * self.width + 2 * self.height)
        return result

    def get_diagonal(self):
        result = ((self.width ** 2 + self.height ** 2) ** .5)
        return result

    def get_picture(self):
        hvezda = '*'
        final = ''
        for i in range(self.height):
            str = self.width * hvezda
            final += f'{str}\n'
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            return final

    def get_amount_inside(self, another_shape):
        if another_shape.height == another_shape.width:
            result = self.get_area() // (another_shape.height**2)
            return result
        else:
            result = self.get_area() // another_shape.get_area()
            return result


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.height = side_length
        self.width = side_length

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side):
        self.side_length = new_side
        self.height = new_side
        self.width = new_side
        return self.side_length

    def set_height(self, new_height):
        self.side_length = new_height
        return self.side_length

    def set_width(self, new_width):
        self.side_length = new_width
        return self.side_length

    def get_diagonal(self):
        result = float(math.sqrt(self.side_length ** 2 + self.side_length ** 2))
        return result

    def get_picture(self):
        hvezda = '*'
        final = ''
        for i in range(self.side_length):
            str = self.side_length * hvezda
            final += f'{str}\n'
        if self.side_length > 50:
            return 'Too big for picture.'
        else:
            return final

    def get_side(self):
        return self.side_length

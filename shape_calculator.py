class Rectangle:
    width = 0
    height = 0
    area = 0
    perimeter = 0
    diagonal = 0
    amount_inside = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __repr__(self):
        if self.width != self.height:
            return f'Rectangle(width={self.width}, height={self.height})'
        else:
            return f'Square(side={self.width})'
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        self.area = self.width * self.height
        return self.area
    def get_perimeter(self):
        self.perimeter = (2*self.width) + (2*self.height)
        return self.perimeter
    def get_diagonal(self):
        self.diagonal = ((self.width ** 2) + (self.height ** 2)) ** (.5)
        return self.diagonal
    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for column in range(self.height):
                for row in range (self.width):
                    picture += '*'
                picture += '\n'
        return picture
    def get_amount_inside(self, shape):
        width, height = shape.width, shape.height
        width_proportion, height_proportion = self.width // width, self.height // height
        self.amount_inside = width_proportion * height_proportion
        return self.amount_inside

class Square(Rectangle):
    def __init__(self, side):
        self.width, self.height = side, side
    def set_side(self, side):
        self.width, self.height = side, side
    def set_height(self, height):
        self.set_side(height)
    def set_width(self, width):
        self.set_side(width)
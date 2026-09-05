import math as m 

class Rectangle():
    def __init__(self,width ,height):
        self.width = width
        self.height = height 

    def set_width(self,width_value):
        self.width = width_value

    def set_height(self,height_value):
        self.height = height_value
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    def get_diagonal(self):
        return m.sqrt((self.width*self.width)+(self.height*self.height))
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return f"Too big for picture."
        line = "*" * self.width + "\n"
        final = line * self.height
        return final

    def get_amount_inside(self,shape):
        horizontal = self.width // shape.width
        vertical = self.height // shape.height
        return horizontal * vertical

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self,width_value):
        self.width = width_value
        self.height = width_value

    def set_height(self,height_value):
        self.width = height_value
        self.height = height_value

    def set_side(self,side):
        self.width = side
        self.height = side
        
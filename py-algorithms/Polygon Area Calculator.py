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
        return f"{self.width},{self.height}"

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return f"Too big for picture."
        title = self.width.center(5, "*")
        output = title + "\n"

    def get_amount_inside(self):
        return 

class Square(Rectangle):
    def __init__(self):
        super().__init__(width ,height)


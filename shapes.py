class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    def draw(self, canvas):
        """
        draws itself into the canves
        """
        #changes a slice of the array with new values
        canvas.data[self.x : self.x + self.side, self.y : self.y + self.side] = self.color


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw(self, canvas):
        """draws itself intp the canvas"""
        #changes a slice of the array with new values
        canvas.data[self.x : self.x +self.height, self.y : self.y + self.width] = self.color



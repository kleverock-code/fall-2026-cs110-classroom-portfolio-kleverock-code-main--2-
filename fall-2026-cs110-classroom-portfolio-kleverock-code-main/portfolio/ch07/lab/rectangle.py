class Rectangle:
    def __init__(self, x, y, h, w):
        """
        Initializes a Rectangle object with non-negative position.
        args:
            x (int/float): x-coordinate
            y (int/float): y-coordinate
            h (int/float): height of the rectangle
            w (int/float): width of the rectangle
        return: None
        """
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)



    def __str__(self):
        return f"(x: {self.x}, (y: {self.y}, (h: {self.h}, (w: {self.w})"

    

    
    
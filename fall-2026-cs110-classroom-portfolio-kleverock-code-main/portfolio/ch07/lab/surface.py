from rectangle import Rectangle


class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Initializes a Surface object with an image filename and a Rectangle.
        args:
            filename (str): path or name of the image file
            x (int/float): x-coordinate
            y (int/float): y-coordinate
            h (int/float): height of the rectangle
            w (int/float): width of the rectangle
        return: None
        """
        self.image = filename
        self.rect = Rectangle(x, y, h, w)

    def getRect(self):
        return self.rect
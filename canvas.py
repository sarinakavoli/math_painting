import numpy as np
from PIL import Image

class Canvas:
    """
    object where all shapes are going to be drawn
    """
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        #Creat a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype = np.uint8)
        #change[0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
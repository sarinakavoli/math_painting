import numpy as np
from PIL import Image
import os

#create 3d numpy array of zeros, then replace zeros(black pixels) with yellow pixels

data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

data[0:3, 0:3] = [255, 0, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

#print("Current working directory:", os.getcwd())
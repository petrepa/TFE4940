from PIL import Image
import numpy as np

im = Image.open('test.png')
p = np.array(im)

print(p)
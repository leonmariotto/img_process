import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from PIL import Image

class ImageProcessor():
  def __init__(self):
    pass

  def load(self, path):
    img = np.array(Image.open(path)) #mpimg.imread(path)
    print (np.array)
    return img

  def display(self, array):
    plt.imshow(array)
    plt.show()

  def save(self, array, path):
    img = Image.fromarray(array)
    img.save(path);

#   def load_arr(self, paths):
#	for file in paths:
#		list(lst_np)
#		lst_np.append(np.array(Image.open(file)))
#	return lst_np

import numpy as np


class ScrapBooker:
    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        dimensions = (dimensions[0] + position[0], dimensions[1] + position[1])
        array = array[position[0] : dimensions[0], position[1] : dimensions[1]]
        return array

    def thin(self, array, n, axis):
        if axis == 0 or axis == 1:
            array = np.delete(array, slice(None, None, n), axis)
        else:
            raise ValueError("Axis must be 0 or 1")
        return array

    def thinundershape(self, array, x, y, shape):
        if shape[0] < array.shape[0]:
            array = np.delete(array, slice(None, None, y), 0)
        if shape[1] < array.shape[1]:
            array = np.delete(array, slice(None, None, x), 1)
        return array

    def thinall(self, array, x, y):
        array = np.delete(array, slice(None, None, y), 0)
        array = np.delete(array, slice(None, None, x), 1)
        return array

    def juxtapose(self, array, n, axis):
        if axis < 0 or axis > 1:
            raise ValueError("Axis must be 0 or 1")
        array = np.concatenate([array for i in range(n)], axis)
        return array

    def mosaic(self, array, dimensions):
        array = np.concatenate([array for i in range(dimensions[0])], 0)
        array = np.concatenate([array for i in range(dimensions[1])], 1)
        return array

    # def concate(self, array, x, y, axis):
    #      for i in range(1, y, x)
    #  		line = np.concatenate([array for i in range(x)], 0)
    #
    #  res = np.concatenate([array for i in range(x)], 0)
    #  res = np.concatenate([array for i in range(y)], 1)
    #  return array

    # def concate_line(self, array, x, axis):
    #  res = np.concatenate(array, 0)
    #  return res

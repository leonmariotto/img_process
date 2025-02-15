"""Module ColorFilter"""

import logging
import numpy as np

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


class ColorFilter:
    """
    Class ColorProcessor
    """

    def __init__(self):
        """
        Init ColorProcessor
        """
        self.logger = logging.getLogger(__name__)

    def invert(self, array):
        a = np.ones_like(array)
        return a - array

    def to_blue(self, array):
        a = np.array(array)
        a[:, :, :2] = 0
        return a

    def to_green(self, array):
        return array * [0, 1, 0]

    def to_red(self, array):
        a = np.array(array)
        a[:, :, 1:] = 0
        return a

    def border(self, array, p):
        a = np.array(array)
        a[:p, :, :] = 0
        a[array.shape[0] - p :, :, :] = 0
        a[:, :p, :] = 0
        a[:, array.shape[1] - p :, :] = 0
        return a

    def celluloid(self, array, thresholds=4):
        a = np.array(array)
        a *= thresholds
        a = a.astype(np.int8)
        a = a.astype(np.float32)
        a /= thresholds
        return a

    def to_grayscale(self, array, arg="weighted"):
        a = np.array(array)
        if arg == "weighted" or arg == "w":
            shape = a.shape
            a *= [0.299, 0.587, 0.114]
            a = np.sum(a, axis=2, keepdims=True)
            a = np.broadcast_to(a, shape)
            return a
        elif arg == "mean" or arg == "m":
            a = np.mean(a, axis=2, keepdims=True)
            a = np.tile(a, (1, 1, 3))
            return a

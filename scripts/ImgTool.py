"""Module ImgTool"""

import logging
import numpy
import matplotlib.pyplot
import PIL.Image

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


class ImgTool:
    """
    Class ImgTool processor
    """

    def __init__(self):
        """
        Init ImgTool
        """
        self.logger = logging.getLogger(__name__)

    def load(self, path: str):
        """
        Return a numpy array from an image path
        """
        img = numpy.array(PIL.Image.open(path))
        # If image is 2D (grayscale), stack it along a new axis to create an RGB image.
        if img.ndim == 2:
            # np.stack takes a sequence of arrays and stacks them along a new axis.
            # Here, we stack the same array three times along the last axis.
            self.logger.debug("Create a rgb channel for grayscall image")
            img = numpy.stack([img] * 3, axis=-1)
        self.logger.debug("Create numpy array from image path [%s]", path)
        return img

    def display(self, array):
        """
        Use matplotlib.pyplot to diplay numpy array
        """
        self.logger.debug("Display numpy array image")
        matplotlib.pyplot.imshow(array)
        matplotlib.pyplot.show()

    def save(self, array, path):
        """
        Save a numpy array into a image file (png)
        """
        img = PIL.Image.fromarray(array)
        img.save(path, format="PNG")
        self.logger.debug("Save numpy array image to path [%s]", path)

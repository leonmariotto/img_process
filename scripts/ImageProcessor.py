"""Module image processor"""

import logging
import matplotlib.pyplot
import numpy
import PIL.Image
import click
from typing import List
import os

from .DataStore import DataStore, Key
from .YamlParser import YamlParser
from .ScrapBooker import ScrapBooker

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


class ImageProcessor:
    """
    Class image processor
    """

    def __init__(self):
        """
        Init ImageProcessor
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

def get_environment_vars(data_store: DataStore):
    """
    Get some environment variables :
        - WORKSPACE_DIRECTORY
    """
    workspace_dir = os.getenv("WORKSPACE_DIR")
    if workspace_dir is None:
        raise ValueError("WORKSPACE_DIR must be exported")
    data_store.add_entry([Key.WORKSPACE_DIR], workspace_dir)


@click.command()
@click.option(
    "--yamls",
    "-y",
    default=[],
    multiple=True,
    type=str,
    help="Yaml configuration, can be done multiple time",
)
@click.option(
    "--output",
    "-o",
    default="image_processor_output.png",
    type=str,
    show_default=True,
    help="Output file",
)
def image_processor(yamls: List[str], output: str):
    """
    A tool to manipulate lot of image
    """
    data_store = DataStore()
    get_environment_vars(data_store)
    yaml_parser = YamlParser(data_store)
    for y in yamls:
        logging.debug("Loading yml {%s}", y)
        yaml_parser.parse(y)
    img_processor = ImageProcessor()
    scrap_booker = ScrapBooker()
    images_path_list = data_store.get_entry([Key.IMAGES_LIST])
    images_content_list = [img_processor.load(img) for img in images_path_list]
    crop_x = int(data_store.get_entry([Key.CROP, Key.END, Key.X]))
    crop_y = int(data_store.get_entry([Key.CROP, Key.END, Key.Y]))
    crop_origin_x = int(data_store.get_entry([Key.CROP, Key.ORIGIN, Key.X]))
    crop_origin_y = int(data_store.get_entry([Key.CROP, Key.ORIGIN, Key.Y]))
    croped_images_content_list = [
        scrap_booker.crop(img, (crop_x, crop_y),
        (crop_origin_x, crop_origin_y)) for img in images_content_list
    ]
    images_content_list = croped_images_content_list
    thin_x = int(data_store.get_entry([Key.THIN, Key.X]))
    thin_y = int(data_store.get_entry([Key.THIN, Key.Y]))
    thined_images_content_list = [
        scrap_booker.thin(img, (thin_x, thin_y)) for img in images_content_list
    ]
    border_size = int(data_store.get_entry([Key.BORDER, Key.SIZE]))
    border_mode = str(data_store.get_entry([Key.BORDER, Key.MODE]))
    borded_images_content_list = [
        scrap_booker.border(img, border_size, border_mode) for img in images_content_list
    ]
    images_content_list = borded_images_content_list
    shape_x = int(data_store.get_entry([Key.SHAPE, Key.X]))
    shape_y = int(data_store.get_entry([Key.SHAPE, Key.X]))
    rows_content_list = []
    for i in range(shape_y):
        rows_content_list.append(
            numpy.concatenate(images_content_list[i * shape_x : (i + 1) * shape_x :], 1)
        )
    final_image_content = numpy.concatenate(rows_content_list[::], 0)
    img_processor.save(final_image_content, output)

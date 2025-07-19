"""Module Concatenator"""

import logging
import numpy
import click
from typing import List
import os

from .DataStore import DataStore
from .YamlParser import YamlParser
from .ScrapBooker import ScrapBooker
from .ImgTool import ImgTool

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


def get_environment_vars():
    """
    Get some environment variables :
        - WORKSPACE_DIRECTORY
    """
    workspace_dir = os.getenv("WORKSPACE_DIR")
    if workspace_dir is None:
        raise ValueError("WORKSPACE_DIR must be exported")


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
def concatenator(yamls: List[str], output: str):
    """
    A tool to concate a lot of image
    """
    get_environment_vars()

    yaml_parser = YamlParser()
    for y in yamls:
        logging.debug("Loading yml {%s}", y)
        yaml_parser.parse(y)
    data_store = DataStore(**yaml_parser.data_store)
    img_processor = ImgTool()
    scrap_booker = ScrapBooker()
    images_path_list = data_store.images_list
    images_content_list = [img_processor.load(img) for img in images_path_list]
    crop_x = int(data_store.crop.end.x)
    crop_y = int(data_store.crop.end.y)
    crop_origin_x = int(data_store.crop.origin.x)
    crop_origin_y = int(data_store.crop.origin.y)
    croped_images_content_list = [
        scrap_booker.crop(img, (crop_x, crop_y), (crop_origin_x, crop_origin_y))
        for img in images_content_list
    ]
    images_content_list = croped_images_content_list
    thin_x = int(data_store.thin.x)
    thin_y = int(data_store.thin.y)
    thined_images_content_list = [
        scrap_booker.thin(img, (thin_x, thin_y)) for img in images_content_list
    ]
    images_content_list = thined_images_content_list
    border_size = int(data_store.border.size)
    border_mode = str(data_store.border.mode)
    borded_images_content_list = [
        scrap_booker.border(img, border_size, border_mode)
        for img in images_content_list
    ]
    images_content_list = borded_images_content_list
    shape_x = int(data_store.shape.x)
    shape_y = int(data_store.shape.x)
    rows_content_list = []
    for i in range(shape_y):
        rows_content_list.append(
            numpy.concatenate(images_content_list[i * shape_x : (i + 1) * shape_x :], 1)
        )
    final_image_content = numpy.concatenate(rows_content_list[::], 0)
    img_processor.save(final_image_content, output)

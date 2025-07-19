"""
Module DataStore
"""

import logging
from typing import List
import os
from pydantic import BaseModel, computed_field

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


class Border(BaseModel):
    size: int
    mode: str


class Shape(BaseModel):
    x: int
    y: int


class Thin(BaseModel):
    x: int
    y: int


class Point(BaseModel):
    x: int
    y: int


class Crop(BaseModel):
    origin: Point
    end: Point


class DataStore(BaseModel):
    border: Border
    thin: Thin
    crop: Crop
    shape: Shape
    images_list: List[str]

    @computed_field
    @property
    def workspace_dir(self) -> str | None:
        return os.getenv("WORKSPACE_DIR")

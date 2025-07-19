"""
Module DataStore
"""

import logging
from typing import List
from enum import Enum

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


class Key(Enum):
    """
    Class Key
    """

    WORKSPACE_DIR = "workspace_dir"
    IMAGES_LIST = "images_list"
    CROP = "crop"
    THIN = "thin"
    SHAPE = "shape"
    ORIGIN = "origin"
    END = "end"
    X = "x"
    Y = "y"
    BORDER = "border"
    MODE = "mode"
    SIZE = "size"


class DataStore:
    """
    Class DataStore
    This class is a wrapper around a dictonary, providing
    some function to manipulate the dict:
        - add_entry: add a new entry, if its already exist raise an exception
        - get_entry: get an entry, if its not exist raise an exception
        - set_entry: set an existing entry, if its not exist raise an exception
    Value of DataStore can be anything except a Dictionnary.
    """

    __TOKEN = ";"

    def __init__(self):
        """
        Init DataStore
        """
        self.logger = logging.getLogger(__name__)
        self.data = {}
        pass

    def __contains__(self, keywords: List[Key]) -> bool:
        """
        Check if the key is registered into the DataStore
        """
        key = self.__key(keywords)
        if key in self.data:
            return True
        return False

    def add_entry(self, keywords: List[Key], value):
        """
        Check if an entry exist, if not add it, otherwise raise
        an exception
        """
        key = self.__key(keywords)
        if key in self.data:
            raise KeyError("Error key is already in DataStore")
        self.data[key] = value

    def get_entry(self, keywords: List[Key]):
        """
        Check if an entry exist, if not raise an exception
        otherwise return the value
        """
        key = self.__key(keywords)
        if key not in self.data:
            raise KeyError("Error key is already in DataStore")
        return self.data[key]

    def set_entry(self, keywords: List[Key], value):
        """
        Check if an entry exist, if not raise an exception
        otherwise set the entry to the value
        """
        key = self.__key(keywords)
        if key not in self.data:
            raise KeyError("Error key is already in DataStore")
        self.data[key] = value

    @staticmethod
    def __key(keywords: List[Key]) -> str:
        """
        Create a string from a list of Key
        The string is the effective entry in data dictionary
        Use __TOKEN has separator
        """
        if not keywords:
            raise KeyError("Empty key")
        return DataStore.__TOKEN.join([str(key.value) for key in keywords])

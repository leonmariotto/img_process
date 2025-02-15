"""
Module YamlParser
"""

import logging
from typing import List, Dict
import strictyaml
from .DataStore import DataStore, Key

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

class YamlParserError(Exception):
    """
    Custom class for yaml parsing error
    """

class YamlParser():
    """
    Class YamlParser
    """
    def __init__(self, data_store:DataStore):
        """
        Init YamlParser
        """
        self.logger = logging.getLogger(__name__)
        self.data_store = data_store
  
    def parse(self, path:str):
        self.logger.debug("Parse YAML file [%s]", path)

        # Read file content into string
        try:
            with open(path, "r", encoding="utf-8") as yaml_file:
                yaml_text = yaml_file.read()
        except OSError as err:
            self.logger.error("Error opening the file [%s]", path)
            raise YamlParserError from err
        # Validate YAML and parse it into a dict
        try:
            yaml_data = strictyaml.load(yaml_text).data
        except strictyaml.YAMLError as err:
            self.logger.error("Error parsing the yaml [%s]", path)
            raise YamlParserError from err
        YamlParser.__add_keys(yaml_data, self.data_store, [])

    @staticmethod
    def __add_keys(
        data,
        data_store:DataStore,
        key: List[Key],
    ):
        """
        Recursively add key value pair into the dict
        """
        for curr_key, value in data.items():
            # Push current key
            key.append(Key(curr_key))
            if isinstance(value, Dict):
                YamlParser.__add_keys(value, data_store, key)
            else:
                # Add the edge value
                data_store.add_entry(key, value)
            # Pop current key
            key.pop()

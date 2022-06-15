import json
from xml.etree import ElementTree as etree
from abc import abstractmethod, ABC


class AbstractConnector(ABC):
    @property
    @abstractmethod
    def parsed_data(self):
        """Return parsed_data"""


class JSONConnector(AbstractConnector):
    def __init__(self, filepath):
        self.json = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.json = json.load(f)

    @property
    def parsed_data(self):
        return self.json


class XMLConnector(AbstractConnector):
    def __init__(self, filepath):
        self.tree = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.tree = etree.parse(f)

    @property
    def parsed_data(self):
        return self.tree


class ConnectorsFactory:
    def get_connector(self, file_name):
        try:
            if "json" in file_name:
                return JSONConnector(file_name)
            if "xml" in file_name:
                return XMLConnector(file_name)
            raise AssertionError("Requested file type is not supported")
        except Exception as e:
            raise Exception(e)

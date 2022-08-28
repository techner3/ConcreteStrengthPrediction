from collections import namedtuple
from logging import logger 
from src.utils import read_yaml
from src.constant import CONFIG_PATH
class Configuration:

    def __init__(self):
        
        self.config=read_yaml(CONFIG_PATH)
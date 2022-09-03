from configs import LOGGING_SETUP
from os import name as os_name, system as terminal
import logging


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


class Logging:
    log_format = LOGGING_SETUP["log_format"]
    filename = LOGGING_SETUP["filename"]
    filemode = LOGGING_SETUP["filemode"]
    level = LOGGING_SETUP["level"]
    
    log_levels = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    
    logging.basicConfig(filename, filemode, level, log_format)
    
    def __init__(self, log_level="Debug", log_message="defualt message"):
        self.log_level = log_level
        self.log_message = log_message
        
    @property
    def log_level(self):
        return self._log_level
    
    @log_level.setter
    def log_level(self, level: str):
        if level.lower() in Logging.log_levels:
            self._log_level = level
        logging.log(Logging.log_levels['error'], f"The Log_level of {level} is wrong.")
        
    def LOG(self, log_level, log_message) -> None:
        logging.log(log_level, log_message)
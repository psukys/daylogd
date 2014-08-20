import logging
import json
import os.path

# The configuration file has coordinated data and has to be in the same folder as the project
#It consists of paths to other configs
class Defaults:
    def get_config(self):
    """
    Finds the main configuration file
    """
        pass
    
    def get_logger_config(self):
    """
    Finds the main logger configuration file
    """
        #TODO: go smart with scanning project's child folders and parents folders for logger configuration file.
        #scan should be capped to time limit or the limit should be defined by user himself
        pass

    def set_logger_config_default(self):
    """
    Sets the logger configuration file with default values
    """
        pass

    def set_config_default(self):
    """
    Sets the configuration file with default values
    """
        pass

import os
import json


class Config:

    """
    """

    def __init__(self):
        pass

    def get_main_config(self):
        with open(os.path.join(get_settings_dir(),
                               "conf.json")) as file_stream:
            json_data = json.load(file_stream)
        return json_data

    def create_main_config(self):
        """Creates main config

        with default values (defined in this function),
        saves conf.json file to settings with them
        and returns the json object with these values

        Returns:
            json object with default configuration values

        """
        config = {"logging":
                  {"folder": "log",
                   "format":
                   "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                   "level": "20"},
                  "daylog": {"folder": "daylog",
                             "format":
                             "%(asctime)s: %(topic)s\n %(message)s",
                             "datefmt": "%Y-%m-%d, %H:%M:%S"}}
        json.dump(config, open(
            os.path.join(get_settings_dir,
                         "conf.json"), "w+"), indent=4, sort_keys=True)
        return json.dump(config, fp=True)

    def get_settings_dir(self):
        """Gets the settings directory
        That's where configuration files are saved

        Returns:
            location for settings directory
        """

        settings = "settings"
        current_directory = os.path.dirname(os.path.realpath(__file__))
        if os.path.isdir(os.path.join(current_directory, settings)):
            return os.path.join(current_directory, settings)

        # TODO: a more idiomatic python approach
        for i in range(5):
            current_directory = os.path.join(current_directory, os.pardir)
            if os.path.isdir(os.path.join(current_directory, settings)):
                return os.path.normpath(os.path.join(current_directory, settings))

        # if nothing's found, use current directory
        return_dir = os.path.dirname(os.path.realpath(__file__))
        os.mkdir(os.path.join(return_dir, settings))
        return os.path.join(return_dir, settings)

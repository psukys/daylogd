import os
import json
import logging

class Config:

    """
    The purpose of this class is to work with settings and configuration files
    Primarily there's only conf.json, but the user might want to indicate
    other settings files, which might come in hand for him
    """

    def __init__(self):
        logging.basicConfig(filename=self.__class__.__name__+".log", level=logging.INFO)
        logging.info("Logger initiated")

    def get_main_config(self):
        """Returns main config in JSON object
        """
        conf_file = "conf.json"
        conf_path = os.path.join(self.get_settings_dir(), conf_file)
        if not os.path.isfile(conf_path):
            logging.warning("conf.json not found in %s, initiating default one" % conf_path)
            self.create_main_config()

        with open(conf_path) as file_stream:
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
            os.path.join(self.get_settings_dir(),
                         "conf.json"), "w+"), indent=4, sort_keys=True)
        return json.dumps(config)

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
        logging.info("Settings folder not found, creating in current directory")
        return_dir = os.path.dirname(os.path.realpath(__file__))
        os.mkdir(os.path.join(return_dir, settings))
        return os.path.join(return_dir, settings)

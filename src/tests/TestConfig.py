import unittest  # unittest library
import os  # for directory and files creation, deletion
import sys
import shutil
import json
# testing object: Config.py
from Config import Config


class TestConfig(unittest.TestCase):

    def setUp(self):
        # Keeping a list of created directories and files
        # which will later be deleted (no poluting after test execution)
        self.created_dirs = []
        self.created_files = []

    def tearDown(self):
        # Iterate through created directories and files to delete them
        # reason: no polution after test execution
        for d in self.created_dirs:
            if os.path.isdir(d):
                shutil.rmtree(d)

        for f in self.created_files:
            if os.path.isfile(f):
                os.remove(f)

    def test_get_settings_dir_current(self):
        """
        Tests the finding of settings directory
        Test cases:
        _1. settings directory is in current (.) directory_
        2. settings directory is in parent directory
        """
        test_object = Config()
        settings_name = "settings"

        current_directory = os.path.abspath(
            os.path.dirname(sys.modules[Config.__module__].__file__))
        settings_directory = os.path.join(current_directory, settings_name)

        # create a settings directory in current directory if there's none
        if not os.path.isdir(settings_directory):
            os.mkdir(settings_directory)
            self.created_dirs.append(settings_directory)

        self.assertEqual(test_object.get_settings_dir(), settings_directory)

    def test_get_settings_dir_parent(self):
        """
        Tests the finding of settings directory
        Test cases:
        1. settings directory is in current (.) directory
        _2. settings directory is in parent directory_
        """
        test_object = Config()
        settings_name = "settings"

        current_directory = os.path.abspath(
            os.path.dirname(sys.modules[Config.__module__].__file__))
        parent_directory = os.path.normpath(
            os.path.join(current_directory, os.path.pardir))
        settings_directory = os.path.join(parent_directory, settings_name)

        # create a settings directory in parent directory if there's none
        if not os.path.isdir(settings_directory):
            os.mkdir(settings_directory)
            self.created_dirs.append(settings_directory)

        self.assertEqual(test_object.get_settings_dir(), settings_directory)

    def test_create_main_config_json_object(self):
        """
        Tests the creation of conf.json file
        Test cases:
        _1. Check if it is formattable JSON object_
        2. Create conf.json in current directory
        3. Create conf.json in parent dir
        """
        test_object = Config()
        settings_name = "settings"
        config_name = "conf.json"
        conf_file_existed = False # this is a flag, for reverting test conf.json file

        current_directory = os.path.abspath(
            os.path.dirname(sys.modules[Config.__module__].__file__))
        settings_directory = os.path.join(current_directory, settings_name)
        config_directory = os.path.join(settings_directory, config_name)
        tmp_config_directory = os.path.join(settings_directory, "test_tmp_conf.json")

        if not os.path.isdir(settings_directory):
            os.mkdir(settings_directory)
            self.created_dirs.append(settings_directory)

        if os.path.isfile(config_directory):
            conf_file_existed = True
            os.rename(config_directory, tmp_config_directory)


        test_object.create_main_config()
        #at this point it is expected that in settings folder there should be a configuration file conf.json
        with open(os.path.join(settings_directory, "conf.json")) as file_stream:
            json_data = json.load(file_stream) #this will throw ValueError when bad format happens- that is good
        
        #maybe add a mechanism for reverting these changes
        if conf_file_existed:
            os.remove(config_directory)
            os.rename(tmp_config_directory, config_directory)



    def test_create_main_config_current_directory(self):
        """
        Tests the creation of conf.json file
        Test cases:
        _1. Check if it is formattable JSON object_
        2. Create conf.json in current directory
        3. Create conf.json in parent dir
        """
        raise NotImplementedError("Not implemented")

    def test_create_main_config_parent_directory(self):
        """
        Tests the creation of conf.json file
        Test cases:
        _1. Check if it is formattable JSON object_
        2. Create conf.json in current directory
        3. Create conf.json in parent dir
        """
        raise NotImplementedError("Not implemented")

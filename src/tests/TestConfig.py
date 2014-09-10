import unittest #unittest library
import os #for directory and files creation, deletion
import sys
import shutil
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
        # TODO: Chnage None to path where test object is ran from
        current_directory = os.path.abspath(os.path.dirname(sys.modules[Config.__module__].__file__))
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
        # TODO: Change None to path where test object is ran from
        current_directory = os.path.abspath(os.path.dirname(sys.modules[Config.__module__].__file__))
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
        raise "Not implemented"

    def test_create_main_config_current_directory(self):
        """
        Tests the creation of conf.json file
        Test cases:
        _1. Check if it is formattable JSON object_
        2. Create conf.json in current directory
        3. Create conf.json in parent dir
        """
        raise "Not implemented"

    def test_create_main_config_parent_directory(self):
        """
        Tests the creation of conf.json file
        Test cases:
        _1. Check if it is formattable JSON object_
        2. Create conf.json in current directory
        3. Create conf.json in parent dir
        """
        raise "Not implemented"
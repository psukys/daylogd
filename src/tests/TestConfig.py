import unittest #unittest library
import os #for directory and files creation, deletion
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
            os.rmdir(d)

        for f in self.created_files:
            os.remove(f)

    def test_get_settings_dir_current(self):
        """
        Tests the finding of settings directory
        Test cases:
        _1. settings directory is in current (.) directory_
        2. settings directory is in parent directory
        3. settings directory is in child directory
        """
        test_object = Config()
        settings_name = "settings"
        # TODO: Chnage None to path where test object is ran from
        current_directory = os.path.dirname(os.path.realpath(None))
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
        3. settings directory is in child directory
        """
        test_object = Config()
        settings_name = "settings"
        # TODO: Change None to path where test object is ran from
        current_directory = os.path.dirname(os.path.realpath(None))
        parent_directory = os.path.normpath(
            os.path.join(current_directory, os.path.pardir))
        settings_directory = os.path.join(parent_directory, settings_name)

        # create a settings directory in parent directory if there's none
        if not os.path.isdir(settings_directory):
            os.mkdir(settings_directory)
            self.created_dirs.append(settings_directory)

        self.assertEqual(test_object.get_settings_dir(), settings_directory)

    def test_get_settings_dir_child(self):
        """
        Tests the finding of settings directory
        Test cases:
        1. settings directory is in current (.) directory
        2. settings directory is in parent directory
        _3. settings directory is in child directory_
        """
        test_object = Config()
        settings_name = "settings"
        child_name = "test_child"
        # TODO: Change None to path where test object is ran from
        current_directory = os.path.dirname(os.path.realpath(None))
        child_directory = os.path.join(current_directory, child_name)

        if not os.path.isdir(child_directory):
            os.mkdir(child_directory)
            self.created_dirs.append(child_directory)

        settings_directory = os.path.join(child_directory, settings_name)

        if not os.path.isdir(settings_directory):
            os.mkdir(settings_directory)
            self.created_dirs.append(child_directory)

        self.assertEqual(test_object.get_settings_dir(), settings_directory)

import unittest
import logging
# testing object: Config.py
from Config import Config


class TestConfig(unittest.TestCase):

    def setUp(self):
        # for cleaning purposes
        self.created_dirs = []
        self.created_files = []

    def tearDown(self):
        for d in self.created_dirs:
            os.rmdir(d)

        for f in self.created_files:
            os.remove(f)

    def test_get_settings_dir_current(self):
        """
        Tests the finding of settings directory
        Test cases:
        1. settings directory is in current (.) directory
        2. settings directory is in parent directory
        3. settings directory is in child directory
        """
        test_object = Config()
        settings_name = "settings"
        current_directory = os.path.dirname(os.path.realpath(__file__))
        settings_directory = os.path.join(current_directory, settings_name)
        
        #create a settings directory in current directory if there's none
        if not os.path.isdir(settings_directory):
            os.mkdir(settings_directory)
            self.created_dirs.append(settings_directory)

        self.assertEqual(test_object.get_settings_dir, settings_directory)
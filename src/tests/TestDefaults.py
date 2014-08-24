import unittest #testing
import os #for manipulating with filesystem
from Defaults import Defaults #testing object


class TestDefaults(unittest.TestCase):

	def setUp(self):
		pass

	def test_get_config(self):
		self.fail("Not implemented")

	def test_get_logger_config(self):
		self.fail("Not implemented")

	def test_set_logger_config_default(self):
		self.fail("Not implemented")

	def test_set_config_default(self):
		self.fail("Not implemented")

	def test_get_settings_dir(self):
		self.fail("Not implemented")

	def test_find_dir(self):
		'''
		Tests:
		1. Find a dir which is in current dir
		2. Find a dir which is in child dir
		3. Find a dir which is in parent dir
		'''
		defaults = Defaults()
		#1. Current dir
		curr_dir_name = "test_curr_dir"

		if not os.path.exists(curr_dir_name):
			os.mkdir(curr_dir_name)

		test_dir = defaults.find_dir(".", curr_dir_name, 10)
		self.assertEqual(os.path.abspath(curr_dir_name), test_dir,
						 "Current dir does not match")
		#don't delete curr dir yet, it's needed for child dir test
		
		#2. Child dir
		child_dir_name = "test_child_dir"

		if not os.path.exists(os.path.join(curr_dir_name, child_dir_name)):
			os.mkdir(os.path.join(curr_dir_name, child_dir_name))

		test_dir = defaults.find_dir(".", child_dir_name, 10)
		self.assertEqual(os.path.abspath(os.path.join(curr_dir_name,
													  child_dir_name),
						 test_dir,
						 "Child dir does not match"))
		os.rmdir(child_dir_name)
		os.rmdir(curr_dir_name)
		
		#3. Parent dir
		parent_dir_name = "test_parent_dir"

		if not os.path.exists(os.path.join("..", parent_dir_name)):
			os.mkdir(os.path.join("..", parent_dir_name))

		test_dir = defaults.find_dir(".", parent_dir_name, 10)
		self.assertEqual(os.path.join("..", parent_dir_name),
						 test_dir,
						 "Parent dir does not match")
		os.rmdir(os.path.join("..", parent_dir_name))

import unittest #testing
import os #for manipulating with filesystem
from Defaults import Defaults #testing object


class TestDefaults(unittest.TestCase):

	def setUp(self):
		#test_find_dir init
		self.curr_dir_name = "test_curr_dir"
		self.child_dir_name = "test_child_dir"
		self.parent_dir_name = "test_parent_dir"
		
		#test_get_settings_dir init
		self.settings_dir_parent = "test_settings_parent"
		self.settings_dir = "settings"
		self.conf_file = "conf.json"

	def tearDown(self):
		#test_find_dir clearance
		if os.path.exists(os.path.join(self.curr_dir_name,
									   self.child_dir_name)):
			os.rmdir(os.path.join(self.curr_dir_name, self.child_dir_name))
		if os.path.exists(self.curr_dir_name):
			os.rmdir(self.curr_dir_name)
		if os.path.exists(os.path.join("..", self.parent_dir_name)):
			os.rmdir(os.path.join("..", self.parent_dir_name))

		#test_get_settings_dir clearance

	def test_get_config(self):
		self.fail("Not implemented")

	def test_get_logger_config(self):
		self.fail("Not implemented")

	def test_set_logger_config_default(self):
		self.fail("Not implemented")

	def test_set_config_default(self):
		self.fail("Not implemented")

	def test_get_settings_dir(self):
		'''
		Test steps:
		1. Create settings dir
		2. Create conf.json dummy file 
		3. validate tested method returns settings dir
		'''
		# preparation
		defaults = Defaults()
		if not os.path.exists(self.settings_dir_parent):
			os.mkdir(self.settings_dir_parent)
		if not os.path.exists(os.path.join(self.settings_dir_parent,
										   self.settings_dir)):
			os.mkdir(os.path.join(self.settings_dir_parent,
								  self.settings_dir))
		if not os.path.exists(os.path.join(self.settings_dir_parent,
										   self.settings_dir,
										   self.conf_file)):
			open(os.path.join(self.settings_dir_parent, self.settings_dir,
							  self.conf_file), 'a')

		test_settings_dir = defaults.get_settings_dir()
		self.assertEqual(test_settings_dir, 
						 os.path.abspath(
						 	os.path.join(self.settings_dir_parent,
						 				 self.settings_dir,
						 				 self.conf_file
						 )), "Settings folder is wrong")

	def test_find_dir(self):
		'''
		Tests steps:
		1.1 Create dir in current dir
		1.2 Find a dir which is in current dir
		2.1 Create dir in child dir
		2.2 Find a dir which is in child dir
		3.1 Create dir in parent dir
		3.2 Find a dir which is in parent dir
		'''
		defaults = Defaults()

		#1. Current dir
		if not os.path.exists(self.curr_dir_name):
			os.mkdir(self.curr_dir_name)

		test_dir = defaults.find_dir(".", self.curr_dir_name, 10)
		self.assertEqual(os.path.abspath(self.curr_dir_name), test_dir,
						 "Current dir does not match")
		#don't delete curr dir yet, it's needed for child dir test

		#2. Child dir
		if not os.path.exists(os.path.join(self.curr_dir_name,
										   self.child_dir_name)):
			os.mkdir(os.path.join(self.curr_dir_name, self.child_dir_name))

		test_dir = defaults.find_dir(".", self.child_dir_name, 10)
		self.assertEqual(os.path.abspath(os.path.join(self.curr_dir_name,
													  self.child_dir_name),
						 test_dir,
						 "Child dir does not match"))

		#3. Parent dir
		if not os.path.exists(os.path.join("..", parent_dir_name)):
			os.mkdir(os.path.join("..", parent_dir_name))

		test_dir = defaults.find_dir(".", parent_dir_name, 10)
		self.assertEqual(os.path.join("..", parent_dir_name),
						 test_dir,
						 "Parent dir does not match")
		os.rmdir(os.path.join("..", parent_dir_name))

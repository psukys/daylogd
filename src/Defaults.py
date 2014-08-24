import logging
import json
import os
from datetime import date


# The configuration file has coordinated data and
#has to be in the same folder as the project
#It consists of paths to other configs
class Defaults:
	def __init__(self):
		self.setup_logger(20, "%(asctime)s: %(topic)s\n %(message)s")

	def setup_logger(self, level, log_format):
		"""
		Sets up a logger instance.
		If logfolder is specified logs are saved day wise
		Args:
			level: logging level
			format: logging format
			logfolder: optional - folder to save logs
		"""
		# TODO: initiate independent initialization process logger,
		# update with setup_logger later. This is needed for full verbose mode
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(level)

		#formatter
		formatter = logging.Formatter(log_format)

		#console handler
		ch = logging.StreamHandler()
		ch.setLevel(level)
		ch.setFormatter(formatter)
		self.logger.addHandler(ch)

		#file handler
		#logfile for current day
		logfile = date.strftime(date.today(), "%Y-%m-%d") + ".log"
		#os.path.join for intelligent joining of paths
		fh = logging.FileHandler(logfile)
		fh.setLevel(level)
		fh.setFormatter(formatter)
		self.logger.addHandler(fh)

	def get_config(self):
		"""
		Finds the main configuration
		"""
		self.logger.info("Loading main configuration file")
		try:
			settingsDir = self.get_settings_dir()
			file = open
		except IOError as err:
			pass

	def get_logger_config(self):
		"""
		Finds the main logger configuration file
		"""
		#TODO: go smart with scanning project's child folders and
		#parents folders for logger configuration file.
		#scan should be capped to time limit or the limit should
		#be defined by user himself
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

	def get_settings_dir (self, search_dirs=10):
		"""
		Gets the project's settings directory
		By default searches in 10 directories for Settings folder
		"""
		curr_dir = os.getcwd()
		#use self.find_dir
		while(search_dirs > 0 and not found):
			#checks if it exists and is a directory
			if os.path.isdir(os.path.join(curr_dir, "settings")):
				found = True
				return curr_dir
			else:
				for root, dirs, files in os.walk("."):
					for d in dirs:
						os.chdir

	def find_dir(self, curr_dir, dir_to_find, dirs_left):
		if dirs_left == 0:
			return None

		#the checkpoint - settings folders
		# TODO: checkpoint with additional syntax check for main config
		if os.path.isdir(os.path.join(curr_dir, dir_to_find)):
			return os.path.join(curr_dir, dir_to_find)
		else:
			#go down to subdirs
			for root, dirs, files in os.walk(curr_dir):
				for d in dirs:
					dirs_left = dirs_left - 1
					found_dir = find_dir(d, dir_to_find, dirs_left)
					if found_dir:
						return found_dir

			#go up 

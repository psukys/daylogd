import os.path
import subprocess
import json
import logging
from datetime import date
from Config import Config

class Daylogd:
	"""
	Day logging class.
	It's principle is parsing user input and appending to current day, which is defined in config
	"""

	def __init__(self):
		self.config = Config()
		#TODO: tasks
		self.logger = logging.getLogger(__name__)

	def read_config(self):
		"""
		Checks for configuration file else creates default
		"""
		# TODO: add support for configuration file externalisation. Config for config?? Maybe self source edit?
		#currently static - homebrew right near the src file
		conf_file = "conf.json"
		if os.path.isfile(conf_file):
			#reads config
			conf_json = json.load(open(conf_file))
			print("Config json loaded")
		else:
			#creates defaults
			conf_json = self.create_default_config(conf_file)
			print("New config created and loaded")
		self.log_conf = conf_json["logging"]
		#any other confs?

	@staticmethod
	def create_default_config(file_name):
		"""
		Creates a default configuration file
		Args:
			file: file name, not path
		"""
		config = {"logging": {"folder": "log",
							  "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
							  "level": "20"},
				  "daylog": {"folder": "daylog",
							 "format": "%(asctime)s: %(topic)s\n %(message)s",
							 "datefmt": "%Y-%m-%d, %H:%M:%S"}}
		'''
		critical - 50
		error - 40
		warning - 30
		info - 20
		debug - 10
		notset - 0
		'''

		json.dump(config, open(os.path.join(
			os.path.dirname(os.path.realpath(__file__)),  # current src file path
			file_name), "w+"), indent=4, sort_keys=True)
		return json.dump(config, fp=True)

	def update_config(self):
		"""
		updates current config
		"""
		self.logger.info("Opening configuration for update")
		# get default program for .conf.json
		output = subprocess.check_output("xdg-mime query default text/plain ", shell=True)
		query = output.replace(".desktop", "").strip() + " conf.json"
		subprocess.Popen(query, shell=True).wait()

	def loop(self):
		# index existing daylogs, search internet?
		return 0

	def main(self):
		self.read_config()
		# since conf is in unicode -> convert to int
		self.setup_logger(int(self.log_conf["level"]), self.log_conf["format"], self.log_conf["folder"])
		self.logger.info("Configuration reading and logger set up: DONE")
		'''
		working principle:
		main: works with system configuration
		loop: everything else
		'''
		loop_status = 0
		while loop_status == 0:
			loop_status = self.loop()

		#0 - loop is ok; 1 - change config
		if loop_status == 1:
			self.update_config()

		self.main()


# Start of script, sends the arguments
if __name__ == "__main__":
	d = Daylogd()
	d.main()
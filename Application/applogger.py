import logging
import os
from appexceptions import GeneralException

class AppLoggger():
    def __init__(self, app_name="AppHasNodeName", create_logfile_dir=True, level="DEBUG"):

	logfile_dir = "/var/log/%s" % app_name
	logfile_path = "%s/app.log" % logfile_dir

	if app_name is None:
		raise GeneralException('app_name is none, this has to be a valid name for the application')
	
	if app_name == "":
		raise GeneralException('app_name is empty, this has to be a valid name for the application')

	if create_logfile_dir == True:
		if os.path.exists(logfile_dir) != True:
			os.mkdir(logfile_dir)	

	if os.path.exists(logfile_dir) != True:
		raise GeneralException('The application expected a log diretory to exist, dir=$s' % logfile_dir)


	self.logger = logging.getLogger(app_name)
        self.file_handler = logging.FileHandler(logfile_path)
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	self.file_handler.setFormatter(formatter)
	self.logger.addHandler(self.file_handler) 
	self.logger.setLevel(level)

    def info(self, message=""):
        self.logger.info(message)

    def warning(self, message=""):
        self.logger.info(message)

    def error(self, message=""):
        self.logger.info(message)

    def error(self, message=""):
        self.logger.debug(message)

    def set_level(self, value="INFO"):

	if app_name is Node:
		raise GeneralException('level is none, try DEBUG,ERROR, WARNING, INFO')
	
	if app_name == "":
		raise GeneralException('level is none, try DEBUG,ERROR, WARNING, INFO')

	if app_name != "DEBUG" and app_name != "ERROR" and app_name != "WARNING" and app_name != "INFO" :
		raise GeneralException('level is not a valid value, try DEBUG, ERROR, WARNING, INFO')

        self.logger.setLevel(value)





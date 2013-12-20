

"""Usage:
deploy-os version
deploy-os description
deploy-os name
deploy-os info
deploy-os start
deploy-os stop
deploy-os vm create <name>
deploy-os vm addtogroup <name> <groupname>
start-os -h | --help | --version

"""

from apiservice import apiservice
from docopt import docopt
from exitcode import ExitCode
from appinfo import AppInformation
from appexceptions import GeneralException
from applogger import AppLoggger
from baremetaldeploymentmanager import BareMetalDeploymentManager
import signal
import multiprocessing




class App:
   
    def __init__(self):
	self.bmdm = None
	self.api_service = None
	self.app_logger = None
	self.app_info = None

    def _start_apiservice(self):
	if self.api_service != None:
		raise GeneralException('ApiService is already started')

	self.api_service = apiservice.Service()
	self.api_service.start()

	return ExitCode(0)

    def _start_services(self):
	exit_code = self._start_apiservice()
	return exit_code

    def _process_commands(self, args=None):

	exit_code = ExitCode(0)

	if args is None:
		raise GeneralException('args object is arguments, none this object needs to be filled with command line.')
	

        if args['version'] == True:
		app_info = AppInformation()
		print app_info.get_version()
		return exit_code

        if args['info'] == True:
		app_info = AppInformation(app_logger)
		print app_info.get_all_info()
		return exit_code
	
	if args['start'] == True:
		exit_code = self._start_services()
		return exit_code

	return exit_code

    def start(self):  

	#Lets get app info for later use
	self.app_info = AppInformation()
        
	#Lets create a logger to log messages
	self.app_logger = AppLoggger(app_name=app_info.get_name())
	
	self.app_logger.info("Application %s starting" % self.app_info.get_name())
	self.app_logger.info("Version: %s" % self.app_info.get_version())
	
	#Install signal handler
	#signal.signal(signal.SIGINT, self.handle_signal)
  
        #lets parse some args
        args = docopt(__doc__, version='0.1.1rc')
        
	#Let parse commands and run some code, this will return one application finishes
        exit_code = self._process_commands(args);

	self.app_logger.info("Application %s ending and exiting" % self.app_info.get_name())
	self.app_logger.info("ExitCode.value: %s" % exit_code.get_value())
	self.app_logger.info("ExitCode.description: %s" % exit_code.get_description())

        return exit_code

    def handle_signal(self,signum, frame):
	self.bmdm.stop()
	return
 





	
	



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

from docopt import docopt
from exitcode import ExitCode
from appinfo import AppInformation
from appexceptions import GeneralException
from applogger import AppLoggger
from baremetaldeploymentmanager import BareMetalDeploymentManager
import signal

import time



class App:
   
    def __init__(self):
	self.bmdm = None
	self.started = False
        

    def _process_commands(self, args=None,app_logger=None):

	exit_code = ExitCode(0)

	if args is None:
		raise GeneralException('args object is arguments, None this object needs to be filled with command line.')
	
	
        if args['version'] == True:
		app_info = AppInformation()
		print app_info.get_version()
		return exit_code

        if args['info'] == True:
		app_info = AppInformation(app_logger)
		print app_info.get_all_info()
		return exit_code
	
	if args['start'] == True:
		#app.run(debug = True)
		self.bmdm =  BareMetalDeploymentManager()
		self.bmdm.start()
		return exit_code


	return exit_code

    def start(self):  

	#from mymod import cay	
	#import mymod.cay
	#cay.myprint()
 

	#return ExitCode(0)

	#Lets get app info for later use
	app_info = AppInformation()
        
	#Lets create a logger to log messages
	app_logger = AppLoggger(app_name=app_info.get_name())
	
	app_logger.info("Application %s starting" % app_info.get_name())
	app_logger.info("Version: %s" % app_info.get_version())
	
	#Install signal handler
	#signal.signal(signal.SIGINT, self.handle_signal)
  
        #lets parse some args
        args = docopt(__doc__, version='0.1.1rc')
        
	#Let parse commands and run some code, this will return one application finishes
        exitcode = self._process_commands(args,app_logger=app_logger);

	app_logger.info("Application %s ending and exiting" % app_info.get_name())
	app_logger.info("ExitCode.value: %s" % exitcode.get_value())
	app_logger.info("ExitCode.description: %s" % exitcode.get_description())

        return exitcode

    def handle_signal(self,signum, frame):
	self.bmdm.stop()
	return
	

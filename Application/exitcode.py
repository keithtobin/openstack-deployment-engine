

class ExitCode():
    def __init__(self, exit_code=0, description=""):
        self.current_exit_code = exit_code
	self.description = description

    def get_value(self):
        return self.current_exit_code

    def get_description(self):

        if self.description != "":
		return self.description

        if self.current_exit_code == 0:
		return "This is the normal exit code and means that the application exited with no errors"

        raise DeploymentEngineExceptionException('this exit code is unknown, this should have not happened. A description for the exit code was not put in ExitCode object')

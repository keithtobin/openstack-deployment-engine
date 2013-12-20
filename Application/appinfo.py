

class AppInformation():
    def __init__(self):
        self.version = "1.0.0"
	self.name = "OpenstackDeploymentEngine"
	self.description = "This application deployes Openstack"

    def get_version(self):
        return self.version

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_all_info(self):
	return "%s\n%s\n%s" % (self.name,self.version,self.description)

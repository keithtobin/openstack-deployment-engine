
from multiprocessing import Process
from applogger import AppLoggger
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

class BareMetalDeploymentManager:
   
    def __init__(self, app_logger=None):
        self.app_logger = app_logger
	self.server = None

    @app.route('/')
    def index():
	return "Hello, World!m"

    @app.route('/tasks', methods = ['GET'])
    def get_tasks():
	tasks = [
		{
		        'id': 1,
        		'title': u'Buy groceries',
        		'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        		'done': False
    		},
    		{
        		'id': 2,
        		'title': u'Learn Python',
        		'description': u'Need to find a good Python tutorial on the web', 
        		'done': False
    		}
	]
    	return jsonify( { 'tasks': tasks } )

    @app.route('/tasks', methods = ['POST'])
    def create_task():
        if not request.json or not 'title' in request.json:
            abort(400)

        #task = {
            #'id': tasks[-1]['id'] + 1,
            #'title': request.json['title'],
            #'description': request.json.get('description', ""),
            #'done': False
        #}

	task = {
            'id': 'keithcathy',
        }

        return jsonify( { 'task': task } ), 201


    def start(self):
	app.run(debug = True)
        #self.server = Process(target=app.run)
	#self.server.start()
	return

    def stop(self):
	#self.server.terminate()
	#self.server.join()
	return
 
	

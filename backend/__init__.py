print("Backend Start")
import os
import MockData

from flask import Flask, render_template, send_from_directory
from flask_cors import CORS, cross_origin

import DataAccess.TagAccess as tags_access
import DataAccess.UserAccess as user_access
import DataAccess.MemoryAccess as memory_access

app = Flask(__name__)
CORS(app)

def Response(response):
	return {"response": response} 

#serve static files
@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
	return send_from_directory(os.path.abspath('/app/backend/templates/html'), path)

@app.route('/')
def app_entrypoint():
	return render_template('app.jinja2')

@app.route('/CreateUser')
def CreateUser():
	return Response(user_access.CreateUser(request))

@app.route('/CreateMemory')
def CreateMemory():
	return Response(memory_access.CreateMemory(request))

@app.route('/GetAllTags')
def GetAllTags():
	return Response(tags_access.GetAllTags())

@app.route('/Login')
def Login():
	return Response(user_access.Login(request))

@app.route('/GetUserMemories')
def GetUserMemories():
	return Response(memory_access.GetUserMemories(request))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

print("Backend End")
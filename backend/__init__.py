print("Backend Start")
import os

from flask import Flask, render_template, send_from_directory
from flask_cors import CORS, cross_origin

import Data_Access as access
import MockData
from DB_Engine import session

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

@app.route('/GetAllIngredients')
def GetAllIngredients():
	return Response(access.GetAllIngredients(session))

@app.route('/GetAllMealTypes')
def GetAllMealTypes():
	return Response(access.GetMealTypes(session))

@app.route('/GetRecipeByFilter')
def GetRecipeByFilter():
	return Response(access.GetRecipes(session, request))

@app.route('/GetRecipeById')
def GetRecipeById():
	return Response(access.GetRecipe(session, request))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

print("Backend End")
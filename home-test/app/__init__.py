from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from app.config import app_config
db = SQLAlchemy()

def create_app(config_name):

	#db connection


	app = Flask(__name__)
	api = Api(app)

	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
	app.config.from_object(app_config[config_name])
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	
	API_v1 = '/api/v1'
	
	#resource import area
	
	
	from todo.resources import TodoListsApi, TodoListApi
	api.add_resource(TodoListsApi, os.path.join(API_v1, 'todolists'))
	api.add_resource(TodoListApi, os.path.join(API_v1, 'todolist'), os.path.join('todolist/<int:id>'))
	
	from shopping.resources import ShoppingListsAPI, ShoppingListAPI
	api.add_resource(ShoppingListsAPI, os.path.join(API_v1, 'shoppinglists'))
	api.add_resource(ShoppingListAPI, os.path.join(API_v1, 'shoppinglist', os.path.join(API_v1, 'shoppinglist/<str:id>'))
	
	db.init_app(app)
	return app

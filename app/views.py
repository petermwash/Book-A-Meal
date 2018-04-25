from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

from app.models.users import User, UserSchema
from app.models.meals import Meal, MealSchema
from app.models.orders import Order

app = Flask(__name__)
api = Api(app)

users = [
User(1, "pe", "mw", "pe@gm.cm", "pp", "123")
]
meals = [
Meal(1, "bb", "snacks", 400.00)
]
orders = []

class UserSignup(Resource):

	def post(self):
		info = json.loads(request.data)
		uzer = User(u_id=info.get('u_id'), f_name=info.get('f_name'), 
			l_name=info.get('l_name'),
			email=info.get('email'), 
			u_name=info.get('u_name'), password=info.get('password'))
		users.append(uzer)

		response = jsonify({"message": "User created"})
		response.status_code = 201
		return response

class UserSignin(Resource):

	def post(self, u_id):
		info = json.loads(request.data)
		for user in users:
			if user.u_id == u_id:
				if user.u_name == info.get('u_name')\
				 and user.password == info.get('password'):
					response = jsonify({"message": "User loged in"})
					response.status_code = 200
					return response
				else:
					response = jsonify({
							"message": "wrong username or password"
							})
					response.status_code = 401
					return response
			response = jsonify({"message": "User not found"})
			response.status_code = 404
			return response

class Meals(Resource):

	def get(self):
		if meals == []:
			response = jsonify({"message": "No meals available"})
			response.status_code = 404
			return response
		schema = MealSchema(many = True)
		mealz = schema.dump(meals)
		response = jsonify(mealz.data)
		response.status_code = 200
		return response

	def post(self):
		info = json.loads(request.data)
		meal = Meal(meal_id=info.get('meal_id'),
			meal_name=info.get('meal_name'), 
			meal_category=info.get('meal_category'),
			meal_price=info.get('meal_price'))
		meals.append(meal)
		response = jsonify({"message": "Meal created"})
		response.status_code = 201
		return response

	def put(self, meal_id):
		for meal in meals:
			if meal.meal_id == meal_id:
				meals.remove(meal)
				info = json.loads(request.data)
				meal = Meal(meal_id,
					meal_name=info.get('meal_name'), 
					meal_category=info.get('meal_category'),
					meal_price=info.get('meal_price'))
		meals.append(meal)
		response = jsonify({"message": "Meal updated"})
		response.status_code = 200
		return response


class SingleMeal(Resource):
	def get(self, meal_id):
		for meal in meals:
			if meal.meal_id == meal_id:
				response = jsonify(meal)
				response.status_code = 200
				return response
			response = jsonify({"message": "Not found"})
			response.status_code = 404
			return response
		

api.add_resource(UserSignup, '/api/v1/signup')
api.add_resource(UserSignin, '/api/v1/signin/<int:u_id>')
api.add_resource(Meals, '/api/v1/meals')
api.add_resource(SingleMeal, '/api/v1/meals/<int:meal_id>')

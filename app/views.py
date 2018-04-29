from flask import Flask, request, jsonify, g, abort
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
import json

from app.models.users import User, UserSchema
from app.models.meals import Meal, MealSchema
from app.models.orders import Order, OrderSchema
from app.models.menu import Menu, MenuSchema

auth = HTTPBasicAuth()

app = Flask(__name__)
api = Api(app)

users = [
User("pe", "mw", "pe@gm.cm", "pp", "123")
]
meals = [
Meal("bb", "snacks", 400.00)
]
menu = [
Meal("chai", "breko", 30.00)
]
orders = [
Order("pet", "burger", 5)
]

@auth.verify_password
def verify_password(u_name, password):
	user = User.verify_auth_token(u_name)
	if not user:
	    for user in users:
	    	if user.u_name == u_name:
	    		uzer = user
	    		if not uzer or not uzer.verify_password(password):
			        return False
	g.user = user
	return True

class UserSignup(Resource):

	def post(self):
		f_name = request.json.get('f_name')
		l_name = request.json.get('l_name')
		email = request.json.get('email')
		u_name = request.json.get('u_name')
		password = request.json.get('password')
		if u_name is None or password is None or f_name is None\
				or l_name is None or email is None: 
			response = jsonify({"message": "Missing argument"})
			response.status_code = 400
			return response
		for u in users:
			if u.u_name == u_name:
				response = jsonify({"message": "User already exists"})
				response.status_code = 400
				return response
		uzer = User(f_name, l_name, email, u_name, password)
		users.append(uzer)
		response = jsonify({"message": "User created"})
		response.status_code = 201
		return response

class UserSignin(Resource):

	@auth.login_required
	def post(self):
		u_name = request.json.get('u_name')
		password = request.json.get('password')
		for usr in users:
			if usr.u_name == u_name:
				verify_password(u_name, password)
				token = g.user.generate_auth_token(600)
				response = jsonify({"token": token.decode('ascii'),
									"duration": 600,
									"message": "User loged in"})
				return response
			response = jsonify({
							"message": "Wrong password or username"
							})
			response.status_code = 401
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
		meal_name = request.json.get('meal_name')
		meal_category = request.json.get('meal_category')
		meal_price = request.json.get('meal_price')
		if meal_name is None or meal_category is None\
				or meal_price is None: 
			response = jsonify({"message": "Missing argument"})
			response.status_code = 400
			return response
		meal = Meal(meal_name, meal_category, meal_price)
		meals.append(meal)
		response = jsonify({"message": "Meal added"})
		response.status_code = 201
		return response

	def put(self, meal_id):
		for meal in meals:
			if meal.meal_id == meal_id:
				meals.remove(meal)
				info = json.loads(request.data)
				meal = Meal(
					meal_name=info.get('meal_name'), 
					meal_category=info.get('meal_category'),
					meal_price=info.get('meal_price'))
				meals.append(meal)
				response = jsonify({"message": "Meal updated"})
				response.status_code = 200
				return response

	def delete(self, meal_id):
		for meal in meals:
			if meal.meal_id == meal_id:
				meals.remove(meal)
				response = jsonify({"message": "Meal deleted!"})
				response.status_code = 200
				return response
			response = jsonify({"message": "Meal not found!"})
			response.status_code = 404
			return response

class MenuEndpoints(Resource):

	def post(self):
		meal_id = request.json.get('meal_id')
		meal_name = request.json.get('meal_name')
		meal_category = request.json.get('meal_category')
		meal_price = request.json.get('meal_price')
		if meal_id is None or meal_name is None or meal_category is None\
				or meal_price is None: 
			response = jsonify({"message": "Missing argument"})
			response.status_code = 400
			return response
		meal = Menu(meal_id, meal_name, meal_category, meal_price)
		menu.append(meal)
		response = jsonify({"message": "Meal added to menu"})
		response.status_code = 201
		return response

	def get(self):
		if menu == []:
			response = jsonify({"message": "No meals in menu"})
			response.status_code = 404
			return response
		schema = MealSchema(many = True)
		mn = schema.dump(menu)
		response = jsonify(mn.data)
		response.status_code = 200
		return response

class OrderEndpoints(Resource):

	def post(self):
		order_owner_name = request.json.get('order_owner_name')
		meal_name = request.json.get('meal_name')
		quantity = request.json.get('quantity')
		if order_owner_name is None or meal_name is None\
				or quantity is None: 
			response = jsonify({"message": "Missing argument"})
			response.status_code = 400
			return response
		order = Order(order_owner_name, meal_name, quantity)
		orders.append(order)
		response = jsonify({"message": "Order created"})
		response.status_code = 201
		return response

	def put(self, order_id):
		for order in orders:
			if order.order_id == order_id:
				orders.remove(order)
				info = json.loads(request.data)
				order = Order(order_owner_name=info.get('order_owner_name'), 
					meal_name=info.get('meal_name'),
					quantity=info.get('quantity'))
		orders.append(order)
		response = jsonify({"message": "Order updated"})
		response.status_code = 200
		return response

	def get(self):
		if orders == []:
			response = jsonify({"message": "Order not found"})
			response.status_code = 404
			return response
		schema = OrderSchema(many = True)
		orderz = schema.dump(orders)
		response = jsonify(orderz.data)
		response.status_code = 200
		return response


api.add_resource(UserSignup, '/api/v1/signup')
api.add_resource(UserSignin, '/api/v1/signin')
api.add_resource(Meals, '/api/v1/meals', '/api/v1/meals/<int:meal_id>')
api.add_resource(MenuEndpoints, '/api/v1/menu')
api.add_resource(OrderEndpoints, '/api/v1/orders', '/api/v1/orders/<int:order_id>')

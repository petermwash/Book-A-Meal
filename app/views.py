from flask import Flask, request, jsonify, g
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
orders = []

u_name_table = {u.u_name: u for u in users}
u_id_table = {u.u_id: u for u in users}

@auth.verify_password
def verify_password(u_name, password):
    user = u_name_table.get(u_name)
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

class UserSignup(Resource):

	def post(self):
		info = json.loads(request.data)
		uzer = User(f_name=info.get('f_name'), 
			l_name=info.get('l_name'),
			email=info.get('email'), 
			u_name=info.get('u_name'), password=info.get('password'))
		if info.get('u_name') is None or info.get('password') is None \
				or info.get('f_name') is None \
				or info.get('l_name') is None or info.get('email') is None: 
			response = jsonify({"message": "missing argument"})
			response.status_code = 400
			return response
			uzer.hash_password(info.get('password'))
		users.append(uzer)

		response = jsonify({"message": "User created"})
		response.status_code = 201
		return response

class UserSignin(Resource):

	@auth.login_required
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
		meal = Meal(meal_name=info.get('meal_name'), 
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

	def delete(self, meal_id):
		for meal in meals:
			if meal.meal_id == meal_id:
				meals.remove(meal)
				response = jsonify({"message": "meal deleted"})
				response.status_code = 200
				return response
			response = jsonify({"message": "meal do not exist"})
			response.status_code = 404
			return response

class MenuEndpoints(Resource):

	def post(self):
		info = json.loads(request.data)
		meal = Menu(meal_id=info.get('meal_id'),
			meal_name=info.get('meal_name'), 
			meal_category=info.get('meal_category'),
			meal_price=info.get('meal_price'))
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
		info = json.loads(request.data)
		order = Order(order_owner_name=info.get('order_owner_name'), 
			meal_name=info.get('meal_name'),
			quantity=info.get('quantity'))
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
api.add_resource(UserSignin, '/api/v1/signin/<int:u_id>')
api.add_resource(Meals, '/api/v1/meals', '/api/v1/meals/<int:meal_id>')
api.add_resource(MenuEndpoints, '/api/v1/menu')
api.add_resource(OrderEndpoints, '/api/v1/orders')
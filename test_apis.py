import unittest
import json
import random

from app.views import app

class UserTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
					"u_id":1,
					"f_name":"peter",
					"l_name":"peter",
					"u_name":"peter",
					"admi":False,
					"email":"my.email@gmail.com",
					"password":"123456789"
					 }

	def test_user_creation(self):
		response = self.app.post(
			'/api/v1/signup', data = json.dumps(
				self.data) , content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "User created")
		self.assertEqual(response.status_code, 201)

	def test_user_creation_without_all_fields(self):
		response = self.app.post(
			'/api/v1/signup', data = json.dumps({
				"u_id":1,
				"f_name":"peter",
				"l_name":"peter",
				"u_name":"peter",
				"admi":False,
				"email":"my.email@gmail.com"
				}), content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Missing argument")
		self.assertEqual(response.status_code, 400)

	def test_user_login(self):
		response = self.app.post(
			'/api/v1/signin', data = json.dumps({
				"password": "123",
				"u_name": "pp"
				}) , content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "User loged in")
		self.assertEqual(response.status_code, 200)

	def test_user_login_with_wrong_password_or_username(self):
		response = self.app.post(
			'/api/v1/signin', data = json.dumps({
				"password": "wrongpswd",
				"u_name": "wrong-user"
				}) , content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(response.status_code, 401)
		self.assertEqual(result["message"], "Wrong password or username")

class MealTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
					"meal_id":1,
					"meal_name":"Burger",
					"meal_category":"Snacks",
					"meal_price":400.00
					 }

	def test_meal_addition(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data) , content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Meal added")
	
	def test_meal_addition_without_one_field(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps({
				"meal_id":8,
				"meal_category":"Snacks",
				"meal_price":400.00
				}), content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Missing argument")
		self.assertEqual(response.status_code, 400)	

	def test_get_all_meals(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		response = self.app.get('/api/v1/meals')
		self.assertEqual(response.status_code, 200)

	def test_update_a_meal(self):
		new_data = {
					"meal_id":1,
					"meal_name":"Burger",
					"meal_category":"Snacks",
					"meal_price":550.00
					}
		response = self.app.put(
			'/api/v1/meals/1', data = json.dumps(
				new_data), content_type = 'application/json')
		res = json.loads(response.data)
		self.assertEqual(res["message"], "Meal updated")
		self.assertEqual(response.status_code, 200)

	def test_delete_a_meal(self):
		response = self.app.delete('/api/v1/meals/1')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Meal deleted!")
		self.assertEqual(response.status_code, 200)

class MenuTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
					"meal_id":1,
					"meal_name":"Burger",
					"meal_category":"Snacks",
					"meal_price":400.00
					 }

	def test_meal_addition_to_menu(self):
		response = self.app.post(
			'/api/v1/menu', data = json.dumps(
				self.data) , content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Meal added to menu")

	def test_meal_addition_to_menu_without_one_field(self):
		response = self.app.post(
			'/api/v1/menu', data = json.dumps({
				"meal_id":8,
				"meal_name":"Burger",
				"meal_category":"Snacks"
				}), content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Missing argument")
		self.assertEqual(response.status_code, 400)

	def test_get_menu_of_the_day(self):
		response = self.app.post('/api/v1/menu',
			data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		response = self.app.get('/api/v1/orders')
		self.assertEqual(response.status_code, 200)

class OrderTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
					"order_id":1,
					"order_owner_name":"peter",
					"meal_name": "burger",
					"quantity": 8
					 }

	def test_make_order(self):
		response = self.app.post(
			'/api/v1/orders', data = json.dumps(
				self.data) , content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Order created")
		self.assertEqual(response.status_code, 201)

	def test_make_order_without_one_field(self):
		response = self.app.post(
			'/api/v1/orders', data = json.dumps({
				"order_id":1,
				"owner_name":"peter",
				"meal_name": "burger"
				}), content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Missing argument")
		self.assertEqual(response.status_code, 400)

		

	def test_modify_order(self):
		new_data = {
					"order_id":1,
					"owner_name":"peter",
					"meal_name": "pizza",
					"quantity": 4
					}
		response = self.app.put(
			'/api/v1/orders/1', data = json.dumps(
				new_data), content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["message"], "Order updated")
		self.assertEqual(response.status_code, 200)

	def test_get_all_orders(self):
		response = self.app.post('/api/v1/orders',
			data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		response = self.app.get('/api/v1/orders')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()

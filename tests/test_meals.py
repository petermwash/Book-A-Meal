import unittest
import json

from app.views import app

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
		self.assertEqual(result["meal_id"], 1)
		self.assertEqual(result["meal_name"], "Burger")
		self.assertEqual(result["meal_category"], "Snacks")
		self.assertEqual(result["meal_price"], 400.00)
		self.assertEqual(result["message"], "meal added")
		

	def test_get_all_meals(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		response = self.app.get('/api/v1/meals')
		result = json.loads(response.data)
		self.assertEqual(res["message"], "all meals returned")
		self.assertEqual(response.status_code, 200)
	
	def test_get_one_meal(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result_in_json = json.loads(
			response.data.decode('utf-8').replace("'", "\""))
		result = self.app.get('/api/v1/meals/{}'.format(result_in_json['order_id']))
		self.assertEqual(result["meal_name"], "Burger")
		self.assertEqual(result["meal_category"], "Snacks")
		self.assertEqual(result["meal_price"], 400.00)

	def test_get_meal_that_do_not_exist(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result = self.app.get('/api/v1/meals/5')
		self.assertEqual(result.status_code, 404)
		self.assertEqual(result["message"], "Meal not found!")

	def test_update_a_meal(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
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
		self.assertEqual(res["meal_id"], 550.00)
		self.assertEqual(res["message"], "meal updated")
		self.assertEqual(response.status_code, 200)

	def test_delete_a_meal(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result_in_json = json.loads(
			response.data.decode('utf-8').replace("'", "\""))
		result = self.app.delete('/api/v1/meals/{}'.format(result_in_json['order_id']))
		self.assertEqual(result.status_code, 200)
		res = self.app.get('/api/v1/meals/{}'.format(result_in_json['order_id']))
		self.assertEqual(res.status_code, 404)
		self.assertEqual(res["message"], "Meal deleteed!")

	def test_delete_a_meal_that_do_not_exist(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result = self.app.delete('/api/v1/meals/5')
		self.assertEqual(result.status_code, 404)
		self.assertEqual(result["message"], "Meal not found!")


if __name__ == '__main__':
	unittest.main()
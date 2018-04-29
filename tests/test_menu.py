import unittest
import json

from app.views import app

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

if __name__ == '__main__':
	unittest.main()


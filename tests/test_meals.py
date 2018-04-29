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


if __name__ == '__main__':
	unittest.main()


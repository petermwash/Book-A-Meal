import unittest
import json

from app.views import app

class MealTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
					"meal_id":5856,
					"meal_name":"Burger",
					"meal_category":"Snacks",
					"meal_price":400.00
					 }

	def test_meal_addition(self):
		response = self.app.post(
			'/api/v1/meals', data = json.dumps(
				self.data) , content_type = 'application/json')
		res = json.loads(response.data)
		self.assertEqual(res["meal_id"], 5856)
		self.assertEqual(res["meal_name"], "Burger")
		self.assertEqual(res["meal_category"], "Snacks")
		self.assertEqual(res["meal_id"], 400.00)
		self.assertEqual(res["message"], "meal added")
		self.assertEqual(response.status_code, 201)

	def test_get_all_meals(self):
		response = self.app.get('/api/v1/meals')
		res = json.loads(response.data)
		self.assertEqual(res["message"], "all meals returned")
		self.assertEqual(response.status_code, 200)

	def test_update_a_meal(self):
		new_data = {
					"meal_id":5856,
					"meal_name":"Burger",
					"meal_category":"Snacks",
					"meal_price":550.00
					}
		response = self.app.put(
			'/api/v1/meals<int:mealId>', data = json.dumps(
				new_data), content_type = 'application/json')
		res = json.loads(response.data)
		self.assertEqual(res["meal_id"], 550.00)
		self.assertEqual(res["message"], "meal updated")
		self.assertEqual(response.status_code, 200)

	def test_delete_a_meal(self):
		response = self.app.delete(
			'/api/v1/meals<int:mealId>', data = json.dumps(
				self.data.clear()), content_type = 'application/json')
		res = json.loads(response.data)
		self.assertNotEqual(res["meal_id"], 5856)
		self.assertNotEqual(res["meal_name"], "Burger")
		self.assertNotEqual(res["meal_category"], "Snacks")
		self.assertNotEqual(res["meal_id"], 400.00)
		self.assertEqual(res["message"], "meal deleteed")
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()
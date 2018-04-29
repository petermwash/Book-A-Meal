import unittest
import json
from datetime import datetime

from app.views import app

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
import unittest
import json

from app.views import app

class OrderTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
					"order_id":1,
					"owner_name":"peter",
					"order_items": ['buger', 'pizza']
					 }

	def test_make_order(self):
		response = self.app.post(
			'/api/v1/orders', data = json.dumps(
				self.data) , content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result = json.loads(response.data)
		self.assertEqual(result["order_id"], 1)
		self.assertEqual(result["owner_name"], "peter")
		self.assertEqual(result["order_items"], ['buger', 'pizza'])
		self.assertEqual(result["message"], "Order created")
		

	def test_modify_order(self):
		response = self.app.post(
			'/api/v1/orders', data = json.dumps(
				self.data) , content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		new_data = {
					"order_id":1,
					"owner_name":"peter",
					"order_items": ['buger', 'pizza', 'cofee']
					}
		response = self.app.put(
			'/api/v1/orders/1', data = json.dumps(
				new_data), content_type = 'application/json')
		result = json.loads(response.data)
		self.assertEqual(result["order_items"], ['buger', 'pizza', 'cofee'])
		self.assertEqual(result["message"], "Order updated")
		self.assertEqual(response.status_code, 200)

	def test_get_all_orders(self):
		response = self.app.post('/api/v1/orders',
			data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result = self.app.get('/api/v1/orders')
		self.assertEqual(result["order_id"], 1)
		self.assertEqual(result["owner_name"], "peter")
		self.assertEqual(result["order_items"], ['buger', 'pizza'])
		self.assertEqual(result["message"], "All orders returned")
		self.assertEqual(result.status_code, 200)

	def test_get_one_order(self):
		response = self.app.post('/api/v1/orders',
			data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result_in_json = json.loads(
			response.data.decode('utf-8').replace("'", "\""))
		result = self.app.get(
			'/api/v1/orders/{}'.format(result_in_json['order_id']))
		self.assertEqual(result["owner_name"], "peter")
		self.assertEqual(result["order_items"], ['buger', 'pizza'])
		self.assertEqual(result["message"], "Order returned")
		self.assertEqual(result.status_code, 200)

	def test_get_an_order_that_do_not_exist(self):
		response = self.app.post('/api/v1/orders',
			data = json.dumps(
				self.data), content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result_in_json = json.loads(
			response.data.decode('utf-8').replace("'", "\""))
		res = self.app.get('/api/v1/orders/5')
		self.assertEqual(res["message"], "Order not found")
		self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
	unittest.main()
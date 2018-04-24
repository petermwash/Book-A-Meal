import unittest
import json

from app.views import app

class OrderTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
					"order_id":585689,
					"owner_name":"peter",
					"order_items": ['buger', 'pizza']
					 }

	def test_make_order(self):
		response = self.app.post(
			'/api/v1/orders', data = json.dumps(
				self.data) , content_type = 'application/json')
		res = json.loads(response.data)
		self.assertEqual(res["order_id"], 585689)
		self.assertEqual(res["owner_name"], "peter")
		self.assertEqual(res["order_items"], ['buger', 'pizza'])
		self.assertEqual(res["message"], "order created")
		self.assertEqual(response.status_code, 201)

	def test_modify_order(self):
		new_data = {
					"order_id":585689,
					"owner_name":"peter",
					"order_items": ['buger', 'pizza', 'cofee']
					}
		response = self.app.put(
			'/api/v1/orders<int:orderId>', data = json.dumps(
				new_data), content_type = 'application/json')
		res = json.loads(response.data)
		self.assertEqual(res["order_items"], ['buger', 'pizza', 'cofee'])
		self.assertEqual(res["message"], "order updated")
		self.assertEqual(response.status_code, 200)

	def test_get_all_orders(self):
		response = self.app.get('/api/v1/orders')
		res = json.loads(response.data)
		self.assertEqual(res["message"], "all orders returned")
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()
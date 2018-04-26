import unittest
import json

from app.views import app

class UserTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
					"userId":1,
					"fname":"peter",
					"lname":"peter",
					"uname":"peter",
					"admi":False,
					"email":"my.email@gmail.com",
					"password":"123456789"
					 }

	def test_user_creation(self):
		response = self.app.post(
			'/api/v1/signup', data = json.dumps(
				self.data) , content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result = json.loads(response.data)
		self.assertEqual(result["userId"], 1)
		self.assertEqual(result["fname"], "peter")
		self.assertEqual(result["lname"], "peter")
		self.assertEqual(result["uname"], "peter")
		self.assertEqual(result["admi"], False)
		self.assertEqual(result["email"], "my.email@gmail.com")
		self.assertEqual(result["password"], "123456789")
		self.assertEqual(result["message"], "user created")

	def test_user_login(self):
		response = self.app.post(
			'/api/v1/login', data = json.dumps(
				self.data) , content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result_in_json = json.loads(
			response.data.decode('utf-8').replace("'", "\""))
		result = self.app.get(
			'/api/v1/login/{}'.format(result_in_json['order_id']))
		self.assertEqual(result.status_code, 200)
		self.assertEqual(result["uname"], "peter")
		self.assertEqual(result["password"], "123456789")
		self.assertEqual(result["message"], "user logged in")

	def test_user_login_with_wrong_password_or_username(self):
		response = self.app.post(
			'/api/v1/login', data = json.dumps(
				self.data) , content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result_in_json = json.loads(
			response.data.decode('utf-8').replace("'", "\""))
		result = self.app.get(
			'/api/v1/login/{}'.format(result_in_json['order_id']))
		self.asserNotEqual(result["uname"], "peter")
		self.assertNotEqual(result["password"], "123456789")
		self.assertEqual(result.status_code, 401)
		self.assertEqual(result["message"], "wrong password or username")


	def test_user_login_with_no_password(self):
		response = self.app.post(
			'/api/v1/login', data = json.dumps(
				self.data) , content_type = 'application/json')
		self.assertEqual(response.status_code, 201)
		result_in_json = json.loads(
			response.data.decode('utf-8').replace("'", "\""))
		result = self.app.get(
			'/api/v1/login/{}'.format(result_in_json['order_id']))
		self.asserNotEqual(result["uname"], "")
		self.assertNotEqual(result["password"], "")
		self.assertEqual(result.status_code, 401)
		self.assertEqual(result["message"], "wrong password or username")


if __name__ == '__main__':
	unittest.main()
	

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


if __name__ == '__main__':
	unittest.main()

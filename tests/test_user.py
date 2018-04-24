import unittest
import json

from app.views import app

class UserTestCase(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = app.test_client()
		self.data = {
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
		res = json.loads(response.data)
		self.assertEqual(res["fname"], "peter")
		self.assertEqual(res["lname"], "peter")
		self.assertEqual(res["uname"], "peter")
		self.assertEqual(res["admi"], False)
		self.assertEqual(res["email"], "my.email@gmail.com")
		self.assertEqual(res["password"], "123456789")
		self.assertEqual(res["message"], "user created")
		self.assertEqual(response.status_code, 201)

	def test_user_login(self):
		response = self.app.get('/api/v1/login')
		res = json.loads(response.data)
		self.assertEqual(res["message"], "user logged in")
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()
from flask import Flask
from marshmallow import Schema, fields
from passlib.apps import custom_app_context as pwd_context
import random
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismysupersecrretkeyformyapiauthentications'

class User(object):
	
	def __init__(self, f_name, l_name, email, u_name, password):
		self.u_id = random.randint(1, 500)
		self.f_name = f_name
		self.l_name = l_name
		self.u_name = u_name
		self.password_hash = self.hash_password(password)
		self.admi = False

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

	def generate_auth_token(self, expiration):
		s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
		return s.dumps({ 'u_id': self.u_id })

	@staticmethod
	def verify_auth_token(token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except SignatureExpired:
			return None
		except BadSignature:
			return None
		user = User.query.get(data['u_id'])
		return user

	def __repr__(self):
		return '<User(name={self.u_name!r})>'.format(self=self)

class UserSchema(Schema):
	
	f_name = fields.Str()
	l_name = fields.Str()
	email = fields.Str()
	u_name = fields.Str()
	password = fields.Str()
	admi = fields.Boolean()


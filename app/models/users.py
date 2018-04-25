from marshmallow import Schema, fields, post_load

class User(object):
	
	def __init__(self, u_id, f_name, l_name, email, u_name, password):
		self.u_id = u_id
		self.f_name = f_name
		self.l_name = l_name
		self.u_name = u_name
		self.password = password
		#self.admi = False

	def __repr__(self):
		return '<User(name={self.username!r})>'.format(self=self)

class UserSchema(Schema):
	
	f_name = fields.Str()
	l_name = fields.Str()
	email = fields.Str()
	u_name = fields.Str()
	password = fields.Str()
	#admi = fields.Boolean()


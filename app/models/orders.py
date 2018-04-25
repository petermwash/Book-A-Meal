from marshmallow import Schema, fields, post_load
from datetime import datetime

class Order(object):
	"""docstring for User"""
	def __init__(self, order_id, ordered_on, order_owner_id, meal):
		self.order_id = order_id
		self.order_owner_id = order_owner_id
		self.meal = meal
		self.ordered_on = datetime.date.today()

	def __repr__(self):
		return '<Order(name={self.order_id!r})>'.format(self=self)

class OrderSchema(Schema):
	"""docstring for UserSchema"""
	order_id = fields.Int()
	order_owner_id = fields.Int()
	#meal = fields.object()
	ordered_on = fields.Date()

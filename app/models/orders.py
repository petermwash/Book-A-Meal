from marshmallow import Schema, fields
from datetime import datetime
import random

class Order(object):

	order_items = {}
	
	def __init__(self, order_owner_name, meal_name, quantity):
		self.order_id = 1 #random.randint(1, 500)
		self.order_owner_id = order_owner_name
		self.meal_name = meal_name
		self.quantity = quantity
		self.ordered_on = datetime.today()

	def __repr__(self):
		return '<Order(name={self.order_id!r})>'.format(self=self)

class OrderSchema(Schema):
	
	order_id = fields.Int()
	order_owner_name = fields.Str()
	order_items = fields.Dict()
	ordered_on = fields.Date()

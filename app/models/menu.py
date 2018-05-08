from marshmallow import Schema, fields

class Menu(object):
	
	def __init__(self, meal_id, meal_name, meal_category, meal_price):
		self.meal_id = meal_id
		self.meal_name = meal_name
		self.meal_category = meal_category
		self.meal_price = meal_price

	def __repr__(self):
		return '<Menu(name={self.meal_name!r})>'.format(self=self)

class MenuSchema(Schema):
	
	meal_id = fields.Integer()
	meal_name = fields.Str()
	meal_category = fields.Str()
	meal_price = fields.Float()


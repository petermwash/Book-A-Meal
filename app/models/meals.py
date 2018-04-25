from marshmallow import Schema, fields, post_load

class Meal(object):
	"""docstring for User"""
	def __init__(self, meal_id, meal_name, meal_category, meal_price):
		self.meal_id = meal_id
		self.meal_name = meal_name
		self.meal_category = meal_category
		self.meal_price = meal_price

	def __repr__(self):
		return '<Meal(name={self.meal_name!r})>'.format(self=self)

class MealSchema(Schema):
	"""docstring for UserSchema"""
	meal_id = fields.Integer()
	meal_name = fields.Str()
	meal_category = fields.Str()
	meal_price = fields.Float()


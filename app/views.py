from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

from app.models.users import User, UserSchema

app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
	app.run()
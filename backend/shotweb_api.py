#! /usr/bin/env python

from flask import Flask
from flask_restful import Api
from resources.static_data import StaticData
from resources.parsing import Parsing

app = Flask(__name__)
api = Api(app)

api.add_resource(StaticData, '/static')
api.add_resource(Parsing, '/parsing/<param1>')

if __name__ == '__main__':
    app.run(debug=True)

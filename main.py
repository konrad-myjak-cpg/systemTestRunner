from flask import Flask
from flask_restful import Api
import os

from service.testResults import TestResults

app = Flask(__name__)
api = Api(app)

api.add_resource(TestResults, '/testResults')

if __name__ == '__main__':
    app.run()

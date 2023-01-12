from flask import Flask
import threading
from flask_restful import Api
from service.testResults import TestResults

from adb.adbController import AdbController

adb = AdbController()
app = Flask(__name__)
api = Api(app)

api.add_resource(TestResults, '/testResults')

if __name__ == '__main__':
    thread = threading.Thread(target=app.run)
    thread.start()
    adb.setReversePortRedirection("5000")
    adb.runTestLoop()

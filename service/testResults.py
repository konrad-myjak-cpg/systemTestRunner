import pandas as pd
from flask_restful import Resource, reqparse

testResultsPath = './data/testResults.csv'

class TestResults(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("testName", type=str, required=True)
        parser.add_argument("testResult", type=str, required=True)

        args = parser.parse_args()

        data = pd.read_csv(testResultsPath)

        data = data.append({
            'id': len(data)+1,
            'testName': args['testName'],
            'testResult': args['testResult']
        }, ignore_index=True)
        data.to_csv(testResultsPath, index=False)
        return {'data': data.to_dict()}, 200
# https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example

from flask import Flask, request, jsonify
from flask_restful import reqparse, Api, Resource

from fraud_detection import MatchingEngine

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('fullname', type=str)

# compute matching for one name
class Match(Resource):
    def post(self):
        request.get_json(force=True)
        args = parser.parse_args()
        fullname = str(args['fullname'])
        matching_engine = MatchingEngine(fullname)
        results = matching_engine.get_matches()
        return results

# compute matching 
class MatchSet(Resource):
    def get(self):
        matching_engine = MatchingEngine()
        status = matching_engine.compute_matches()
        return status

##
# Actually setup the Api resource routing here
##
api.add_resource(MatchSet, '/api/matching/all')
api.add_resource(Match, '/api/matching')


if __name__ == '__main__':
    app.run(debug=True)

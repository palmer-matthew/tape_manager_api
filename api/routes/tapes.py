from flask_restful import Resource, reqparse

paramParser = reqparse.RequestParser()
paramParser.add_argument('order', type=str, location='args')
paramParser.add_argument('page', type=int, location='args')
paramParser.add_argument('per_page', type=int, location='args')
paramParser.add_argument('search', type=str, location='args')

class Tapes(Resource):
    def get(self):
        params = paramParser.parse_args()

        if not params['per_page']:
            params['per_page'] = 10
        
        if not params['page']:
            params['page'] = 1


        return { 'routes': '/api/tapes', 'args': params }
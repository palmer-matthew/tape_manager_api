from flask_restful import Resource

class Tapes(Resource):
    def get(self):
        return { 'routes': '/api/tapes' }
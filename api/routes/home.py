from flask_restx import Resource
from api import api

@api.route('/api/')
class Home(Resource):
    def get(self):
        return { 
            'routes': {
                'base': '/api',
                'get-tapes': '/api/tapes',
                'get-tape': '/api/tape/<id:string>',
                'patch-tape': '/api/tape/<id:string>',
                'put-tape': '/api/tape/<id:string>',
                'delete-tape': '/api/tape/<id:string>'
            }
        }
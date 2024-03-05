from flask_restful import Resource

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
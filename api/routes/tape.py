from flask_restful import Resource

class Tape(Resource):
        
    def get(self, id):
        return { 'route': f'/api/tape/{id}' }
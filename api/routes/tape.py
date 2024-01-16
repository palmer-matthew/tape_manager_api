from flask_restful import Resource, reqparse
from api import db
from api.models.tape import TapeMedia

EMPTY_STATUS_CODE = {
    'result' : [],
    'additional': {},
    'message': 'Something went wrong.',
    'code': 500
} 

BAD_STATUS_CODE = {
    'result' : [],
    'additional': {},
    'message': 'Request is Invalid',
    'code': 400
} 

paramParser = reqparse.RequestParser()
paramParser.add_argument('id', type=str, location='form')
paramParser.add_argument('site', type=str, location='form')
paramParser.add_argument('location', type=str, location='form')
paramParser.add_argument('compartment', type=str, location='form')

class Tape(Resource):
    def put(self):
        try:   
            params = paramParser.parse_args()

            for param in params.keys():
                if params[param] is None:
                    return BAD_STATUS_CODE, BAD_STATUS_CODE['code']

            new_record = TapeMedia(media_id=params['id'],site=params['site'],location=params['location'],compartment=params['compartment'])

            db.session.add(new_record)
            db.session.commit()
            
            result = {
                'result' : new_record.to_basic_json(),
                'additional': {},
                'message': 'Tape Media was Added',
                'code': 201
            } 

            return result, result['code']
        except:
            return EMPTY_STATUS_CODE, EMPTY_STATUS_CODE['code']
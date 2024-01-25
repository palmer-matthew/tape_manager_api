from flask_restful import Resource, reqparse
from api import db
from api.models.tape import TapeMedia
from .http_codes import INTERNAL_ERROR_STATUS_CODE, BAD_STATUS_CODE

paramParser = reqparse.RequestParser()
paramParser.add_argument('id', type=str, location='json')
paramParser.add_argument('site', type=str, location='json')
paramParser.add_argument('location', type=str, location='json')
paramParser.add_argument('compartment', type=str, location='json')

class Tape(Resource):
    def put(self):
        try:   
            params = paramParser.parse_args()

            for param in params.keys():
                if not params[param]:
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
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']
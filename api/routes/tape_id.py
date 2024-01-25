from flask_restful import Resource, reqparse
from api import db
from api.models.tape import TapeMedia
from .http_codes import INTERNAL_ERROR_STATUS_CODE, BAD_STATUS_CODE, EMPTY_STATUS_CODE

paramParser = reqparse.RequestParser()
paramParser.add_argument('update', required=True, type=list, location='form')
paramParser.add_argument('id', type=str, location='form')
paramParser.add_argument('site', type=str, location='form')
paramParser.add_argument('location', type=str, location='form')
paramParser.add_argument('compartment', type=str, location='form')

class TapeID(Resource):
    def get(self, id):
        try:
            if id is None:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
            
            result = get_tape_media(id)
            
            return result, result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']
    
    def patch(self, id):
        try:
            if id is None:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
            
            body = paramParser.parse_args()

            if body['update'] is None or body['update'] == []:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
            
            result = patch_tape_media(id, body)
            
            return result, result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']
    
    def delete(self,id):
        try:
            if id is None:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
            
            result = delete_tape_media(id)
            
            return result, result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']
        
    
def get_tape_media(id):
    db_result = TapeMedia.query.filter_by(media_id = id).first()
    if db_result is None:
        return {
            'result' : {},
            'additional': {},
            'message': 'No records were found',
            'code': 204
        }
    return {
        'result' : db_result.to_json(),
        'additional': {},
        'message': 'No records were found',
        'code': 200
    }

def patch_tape_media(id, body_args):

    update_params = {}
    for key in body_args['update']:
        if key == 'id':
            update_params['media_id'] = body_args['id']
        else:
            update_params[key] = body_args[key]

    db_result = TapeMedia.query.filter_by(media_id = id).update(update_params)
    if db_result <= 0:
        return {
            'result' : {},
            'additional': {},
            'message': 'No records were updated',
            'code': 204
        }
    db.session.commit()

    db_result = TapeMedia.query.filter_by(media_id = id).first()
    return {
        'result' : db_result.to_json(),
        'additional': {},
        'message': 'Record was updated',
        'code': 200
    }

def delete_tape_media(id):
    db_result = TapeMedia.query.filter_by(media_id = id).first()
    if db_result is None:
        return {
            'result' : {},
            'additional': {},
            'message': 'No records were found',
            'code': 204
        }
    db.session.delete(db_result)
    db.session.commit()
    return {
        'result' : {},
        'additional': {},
        'message': 'Record was deleted successfully',
        'code': 200
    }


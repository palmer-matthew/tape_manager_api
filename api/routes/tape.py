from flask_restful import Resource
from api import db
from api.models.tape import TapeMedia

EMPTY_STATUS_CODE = {
    'result' : [],
    'additional': {},
    'message': 'Something went wrong.',
    'code': 500
} 


class Tape(Resource):
    def get(self, id):
        try:
            if id is None:
                return EMPTY_STATUS_CODE, EMPTY_STATUS_CODE['code']
            
            result = get_tape_media(id)
            
            return result, result['code']
        except:
            return EMPTY_STATUS_CODE, EMPTY_STATUS_CODE['code']
        
    
def get_tape_media(id):
    db_result = TapeMedia.query.filter_by(media_id == id).first()
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

def post_tape_media():
    pass

def patch_tape_media():
    pass

def delete_tape_media():
    pass

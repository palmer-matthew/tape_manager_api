from flask_restx import Resource, reqparse
from api import api, db
from api.models.tape import TapeMedia
from .http_codes import INTERNAL_ERROR_STATUS_CODE, BAD_STATUS_CODE, NO_CONTENT_CODE, NO_UPDATE_CONTENT_CODE
from ..utils.swagger import tapeid_patch

paramParser = reqparse.RequestParser()
paramParser.add_argument('update', required=True, type=list, location='json', trim=True)
paramParser.add_argument('id', type=str, location='json', trim=True)
paramParser.add_argument('site', type=str, location='json', trim=True)
paramParser.add_argument('location', type=str, location='json', trim=True)
paramParser.add_argument('compartment', type=str, location='json', trim=True)

@api.route('/api/tape/<string:id>')
@api.doc(params={
    'id': 'Media ID for a Tape Record'
})
class TapeID(Resource):
    # @api.doc(responses={
    #     200: 'Record was retrieved successfully',
    #     204: NO_CONTENT_CODE['message'],
    #     400: BAD_STATUS_CODE['message'],
    #     500: INTERNAL_ERROR_STATUS_CODE['message']
    # })
    @api.response(200, 'Record was retrieved successfully')
    def get(self, id):
        try:
            if id is None:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
            
            result = get_tape_media(id)
            
            return result, result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']
    
    @api.doc(responses={
        200: 'Record was retrieved successfully',
        204: NO_UPDATE_CONTENT_CODE['message'],
        400: BAD_STATUS_CODE['message'],
        500: INTERNAL_ERROR_STATUS_CODE['message']
    })
    @api.expect(tapeid_patch)
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
    
    @api.doc(responses={
        200: 'Record was retrieved successfully',
        204: NO_CONTENT_CODE['message'],
        400: BAD_STATUS_CODE['message'],
        500: INTERNAL_ERROR_STATUS_CODE['message']
    })
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
        return NO_CONTENT_CODE
    return {
        'result' : db_result.to_json(),
        'additional': {},
        'message': 'Record was retrieved successfully',
        'code': 200
    }

def patch_tape_media(id, body_args):

    update_params = {}
    for key in body_args['update']:
        if body_args[key] == '' or body_args is None:
            continue
        if key == 'id':
            update_params['media_id'] = body_args[key].upper()
            new_id = body_args['id']
        else:
            update_params[key] = body_args[key].upper()
            new_id = id
    
    if update_params == {}:
        return NO_UPDATE_CONTENT_CODE

    db_result = TapeMedia.query.filter_by(media_id = id).update(update_params)

    if db_result <= 0:
        return NO_UPDATE_CONTENT_CODE

    db.session.commit()

    db_result = TapeMedia.query.filter_by(media_id = new_id).first()
    return {
        'result' : db_result.to_json(),
        'additional': {},
        'message': 'Record was updated',
        'code': 200
    }

def delete_tape_media(id):
    db_result = TapeMedia.query.filter_by(media_id = id).first()

    if db_result is None:
        return NO_CONTENT_CODE
    
    db.session.delete(db_result)
    db.session.commit()
    return {
        'result' : db_result.to_json(),
        'additional': {},
        'message': 'Record was deleted successfully',
        'code': 200
    }


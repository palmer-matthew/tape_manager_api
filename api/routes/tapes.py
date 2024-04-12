from flask_restful import Resource, reqparse
from api import db
from api.models.tape import TapeMedia
from .http_codes import INTERNAL_ERROR_STATUS_CODE, BAD_STATUS_CODE, EMPTY_STATUS_CODE

paramParser = reqparse.RequestParser()
paramParser.add_argument('page', type=int, location='args')
paramParser.add_argument('per_page', type=int, location='args')
paramParser.add_argument('search', type=str, location='args')

pdParser = reqparse.RequestParser()
pdParser.add_argument('records', required=True, type=list, location='json')

patchParser = reqparse.RequestParser()
patchParser.add_argument('update_field', required=True, type=str, location='json')
patchParser.add_argument('update_value', required=True, type=str, location='json')
patchParser.add_argument('records', required=True, type=list, location='json')

class Tapes(Resource):
    def get(self):
        try:
            params = paramParser.parse_args()

            if not params['per_page']:
                params['per_page'] = 10
            
            if not params['page']:
                params['page'] = 1

            if params['search']:
                result = query_db_with_search(page=params['page'],per_page=params['per_page'],searchTerm=params['search'])
            else:
                result = query_db_no_search(page=params['page'],per_page=params['per_page'])      

            return result , result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']
    
    def put(self):
        try:
            params = pdParser.parse_args()

            if params['records'] is None or params['records'] == []:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']

            result = batch_upload_tapes(params['records'])

            return result , result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']

    def patch(self):
        try:
            params = patchParser.parse_args()

            if params['records'] is None or params['records'] == []:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
            
            if params['update_field'] or params['update_field'] == '':
                field = params['update_field']
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
            
            if params['update_value'] or params['update_value'] == '':
                value = params['update_value']
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']

            result = batch_update_tapes(field, value, params['records'])

            return result , result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']

    def delete(self):
        try:
            params = pdParser.parse_args()

            if params['records'] is None or params['records'] == []:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']

            result = batch_delete_tapes(params['records'])

            return result , result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']

def query_db_with_search(page, per_page, searchTerm: str):

    try:
        db_results = TapeMedia.query.filter(TapeMedia.media_id.contains(searchTerm.upper())).paginate(page=page, per_page=per_page)
    except :
        return EMPTY_STATUS_CODE

    if len(db_results.items) > 0:
        results = [record.to_basic_json() for record in db_results.items]
        return {
            'result' : results,
            'additional': {
                'length': len(results),
                'page': db_results.page,
                'total_pages': db_results.pages,
                'per_page': per_page
            },
            'message': 'Records were retrieved successfully',
            'code': 200
        }
    else:
        return EMPTY_STATUS_CODE


def query_db_no_search(page, per_page):
        
    try:
        db_results = TapeMedia.query.paginate(page=page, per_page=per_page)
    except :
        return EMPTY_STATUS_CODE

    if len(db_results.items) > 0:
        results = [record.to_basic_json() for record in db_results.items]
        return {
            'result' : results,
            'additional': {
                'length': len(results),
                'page': db_results.page,
                'total_pages': db_results.pages,
                'per_page': per_page
            },
            'message': 'Records were found successfully',
            'code': 200
        }
    else:
        return EMPTY_STATUS_CODE
    
def batch_upload_tapes(records: list):
    results = []

    if records == []:
        return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
    
    for record in records:
        results.append(TapeMedia(media_id=record['media_id'],site=record['site'],location=record['location'],compartment=record['compartment']))
                  
    db.session.add_all(results)
    db.session.commit()

    db_results = [result.to_basic_json() for result in results]
    return {
        'result' : db_results,
        'additional': {
            'length': len(db_results),
            'page': 1,
            'total_pages': 1,
            'per_page': 1
        },
        'message': 'Records were found successfully',
        'code': 200
    }

def batch_update_tapes(field: str, value: str, records: list):
    pass
    # db.session.commit()
    # return {
    #     'result' : db_results,
    #     'additional': {
    #         'length': len(db_results),
    #         'page': 1,
    #         'total_pages': 1,
    #         'per_page': 1
    #     },
    #     'message': 'Records were found successfully',
    #     'code': 200
    # }

def batch_delete_tapes(ids: list):
    pass
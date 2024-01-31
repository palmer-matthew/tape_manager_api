from flask_restful import Resource, reqparse
from api import db
from api.models.tape import TapeMedia
from .http_codes import INTERNAL_ERROR_STATUS_CODE, BAD_STATUS_CODE, EMPTY_STATUS_CODE

paramParser = reqparse.RequestParser()
paramParser.add_argument('page', type=int, location='args')
paramParser.add_argument('per_page', type=int, location='args')
paramParser.add_argument('search', type=str, location='args')


class Tapes(Resource):
    def get(self):
        #TODO: Implement Error Logging in GET Route
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
    
    def post(self):
        pass

    def patch(self):
        pass

def query_db_with_search(page, per_page, searchTerm: str):

    try:
        db_results = TapeMedia.query.filter(TapeMedia.media_id.startswith(searchTerm.upper())).paginate(page=page, per_page=per_page)
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
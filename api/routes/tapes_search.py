from flask_restx import Resource
from api import api
from api.models.tape import TapeMedia
from .http_codes import INTERNAL_ERROR_STATUS_CODE, BAD_STATUS_CODE, EMPTY_STATUS_CODE

@api.route('/api/tapes/search/<string:searchTerm>')
class TapesSearch(Resource):
    def get(self, searchTerm):
        try:
            if searchTerm is None:
                return BAD_STATUS_CODE, BAD_STATUS_CODE['code']
            
            result = query_db_search(searchTerm)
            
            return result, result['code']
        except:
            return INTERNAL_ERROR_STATUS_CODE, INTERNAL_ERROR_STATUS_CODE['code']

def query_db_search(searchTerm: str):
    try:
        db_results = TapeMedia.query.filter(TapeMedia.media_id.contains(searchTerm.upper()))
    except :
        return EMPTY_STATUS_CODE

    if db_results.count() > 0:
        results = [record.to_basic_json() for record in db_results]
        return {
            'result' : results,
            'additional': {
                'length': len(results),
                'searchTerm': searchTerm
            },
            'message': 'Records were retrieved successfully',
            'code': 200
        }
    else:
        return EMPTY_STATUS_CODE
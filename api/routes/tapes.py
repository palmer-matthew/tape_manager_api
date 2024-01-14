from flask_restful import Resource, reqparse
from api import db
from api.models.tape import TapeMedia

paramParser = reqparse.RequestParser()
paramParser.add_argument('page', type=int, location='args')
paramParser.add_argument('per_page', type=int, location='args')
paramParser.add_argument('search', type=str, location='args')

class Tapes(Resource):
    def get(self):
        try:
            params = paramParser.parse_args()

            if not params['per_page']:
                params['per_page'] = 10
            
            if not params['page']:
                params['page'] = 1

            if not params['search']:
                result = query_db_with_search(page=params['page'],per_page=params['per_page'],searchTerm=params['search'])
            else:
                result = query_db_no_search(page=params['page'],per_page=params['per_page'])      

            return result , result['code']
        except:
            return {
                'result' : [],
                'additional': {},
                'message': 'Something went wrong.',
                'code': 500
            } , 500

def query_db_with_search(page, per_page, searchTerm: str):

    db_results = TapeMedia.query.filter(TapeMedia.media_id.startswith(searchTerm.upper())).paginate(page=page, per_page=per_page)

    if len(db_results.items) > 0:
        results = [record.to_basic_json() for record in db_results.items]
        return {
            'result' : results,
            'additional': {
                'page': db_results.page,
                'total_pages': db_results.pages
            },
            'message': 'Records were retrieved successfully',
            'code': 200
        }
    else:
        return {
            'result' : [],
            'additional': {
                'page': 1,
                'total_pages': 1
            },
            'message': 'No records were found',
            'code': 204
        }


def query_db_no_search(page, per_page):

    db_results = TapeMedia.query.paginate(page=page, per_page=per_page)

    if len(db_results.items) > 0:
        results = [record.to_basic_json() for record in db_results.items]
        return {
            'result' : results,
            'additional': {
                'page': db_results.page,
                'total_pages': db_results.pages
            },
            'code': 200
        }
    else:
        return {
            'result' : [],
            'additional': {
                'page': 1,
                'total_pages': 1
            },
            'message': 'No records were found',
            'code': 204
        }
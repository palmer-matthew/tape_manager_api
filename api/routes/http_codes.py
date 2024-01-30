#HTTP Response templates
INTERNAL_ERROR_STATUS_CODE = {
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

EMPTY_STATUS_CODE = {
    'result' : [],
    'additional': {
        'length': 0,
        'page': 1,
        'total_pages': 1,
        'per_page': 0
    },
    'message': 'No records were found',
    'code': 204
}

NO_CONTENT_CODE = {
    'result' : {},
    'additional': {},
    'message': 'No records were found',
    'code': 204
}

NO_UPDATE_CONTENT_CODE = {
    'result' : {},
    'additional': {},
    'message': 'No records were updated',
    'code': 204
}
from flask_restx import fields, Model
from api import api


## ROUTE WITH ID MODELS

tapeid_patch = api.model('Patch Tape with ID', 
    {
        "update": fields.String(description='field that will be updated in Tape Media', enum=['id','site','compartment','location']),
        "id": fields.String(description='Tape Media id that will be updated if specified', required=False),
        "site": fields.String(description='Tape Media site location that will be updated if specified', required=False),
        "location": fields.String(description='Tape Media location branch that will be updated if specified', required=False),
        "compartment": fields.String(description='Tape Media compartment location will be updated if specified', required=False)
    }
)

tapeid_patch_ok = api.model('Patch Tape with ID Response', {})
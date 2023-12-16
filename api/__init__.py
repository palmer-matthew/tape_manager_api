# Module Imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Custom Modules Imports
from .config import DevApiConfig, ProdApiConfig
from .routes.home import Home
from .routes.tapes import Tapes
from .routes.tape import Tape

# App and API Initialization
app = Flask(__name__)
app.config.from_object(DevApiConfig)
db = SQLAlchemy(app)
api = Api(app)

# API Route Definitions
api.add_resource(Home, '/api')
api.add_resource(Tapes, '/api/tapes')
api.add_resource(Tape, '/api/tape/<string:id>')

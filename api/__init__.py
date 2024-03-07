# Module Imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Custom Modules Imports
from .config import DevApiConfig, ProdApiConfig


# App and API Initialization
app = Flask(__name__)
app.config.from_object(DevApiConfig)
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

# Importing DB Models and routes
from .models import tape
from .routes.home import Home
from .routes.tapes import Tapes
from .routes.tape import Tape
from .routes.tape_id import TapeID
from .routes.tapes_search import TapesSearch

# API Route Definitions
api.add_resource(Home, '/api')
api.add_resource(Tapes, '/api/tapes')
api.add_resource(TapesSearch, '/api/tapes/search/<string:searchTerm>')
api.add_resource(Tape, '/api/tape')
api.add_resource(TapeID, '/api/tape/<string:id>')

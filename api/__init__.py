# Module Imports
from flask import Flask
from flask_restx import Api
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

# tape_manager = api.namespace('tape_manager', description='Tape Manager API')

# Importing DB Models and routes
from .models import tape
from .routes.home import Home
from .routes.tapes import Tapes
from .routes.tape import Tape
from .routes.tape_id import TapeID
from .routes.tapes_search import TapesSearch

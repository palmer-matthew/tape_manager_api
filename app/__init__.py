from flask import Flask
from .config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)

from app import routes
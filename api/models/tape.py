from api import db
from datetime import datetime
from pytz import timezone

class TapeMedia(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    media_id = db.Column(db.String(8), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_date = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)
    site = db.Column(db.String(50), nullable = False)
    location = db.Column(db.String(50), nullable = False)
    compartment = db.Column(db.String(50), nullable = False)

    def __init__(self,media_id: str, site: str, location: str, compartment: str) -> None:
        self.media_id = media_id
        self.site = site
        self.location = location
        self.compartment = compartment

    def to_json(self) -> dict:
        return {
            'media_id': self.media_id,
            'created_date': self.created_date,
            'modified_date': self.modified_date,
            'site': self.site,
            'location': self.location,
            'compartment': self.compartment
        }
    
    def __repr__(self) -> str:
        return '<Media %s>' % self.media_id
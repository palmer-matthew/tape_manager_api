from api import db
from datetime import datetime
from pytz import timezone

class TapeMedia(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    media_id = db.Column(db.String(8), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    site = db.Column(db.String(50), nullable = False)
    location = db.Column(db.String(50), nullable = False)
    compartment = db.Column(db.String(50), nullable = False)

    def __init__(self,media_id: str, site: str, location: str, compartment: str) -> None:
        self.media_id = media_id.upper()
        self.site = site.upper()
        self.location = location.upper()
        self.compartment = compartment.upper()

    def to_json(self) -> dict:
        return {
            'media_id': self.media_id,
            # 'created_date': self.created_date.strftime("%M/%S/%Y"),
            # 'modified_date': self.modified_datestrftime("%M/%S/%Y"),
            'site': self.site,
            'location': self.location,
            'compartment': self.compartment
        }
    
    def to_basic_json(self) -> dict:
        return {
            'media_id': self.media_id
        }
    
    def __repr__(self) -> str:
        return '<Media %s>' % self.media_id
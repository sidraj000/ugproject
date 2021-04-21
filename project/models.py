from .extensions import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
class DataModel(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    cordinates=db.Column(db.String)

class SensorData(db.Model):
    __tablename__ = 'sesno_data'

    id = db.Column(db.Integer, primary_key=True)
    device_id=db.Column(db.String)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    sData = db.Column(JSON)

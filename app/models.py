from app import db
class DataModel(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    cordinates=db.Column(db.String)

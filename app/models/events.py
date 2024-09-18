from app.database import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_date = db.Column(db.DateTime, nullable=False)
    available_spots = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, start_date, available_spots):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.available_spots = available_spots

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.isoformat(),
            'available_spots': self.available_spots
        }
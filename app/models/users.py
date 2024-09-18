from app.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_registered = db.Column(db.DateTime, default=db.func.current_timestamp())
    registed_for_event_id = db.Column(db.Integer, nullable=True)
    
    def __init__(self, name, email, date_registered=None, registed_for_event_id=None):
        self.name = name
        self.email = email
        self.date_registered = date_registered
        self.registed_for_event_id = registed_for_event_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'date_registered': self.date_registered.isoformat() if self.date_registered else None,
            'registed_for_event_id': self.registed_for_event_id
        }
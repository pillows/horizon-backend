from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DB_URI

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.events import events_bp
    app.register_blueprint(events_bp, url_prefix='/api/events')

    with app.app_context():
        db.create_all()

    return app
from flask import Flask, Response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import DB_URI  # Ensure this import is correct

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    # Configure CORS
    CORS(app, resources={r"/api/*": {"origins": '*'}})
    @app.before_request
    def before_request():
        headers = {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'}
        if request.method.lower() == 'options':
            return jsonify(headers), 200
        
    from app.routes.events import events_bp
    app.register_blueprint(events_bp, url_prefix='/api/events')

    with app.app_context():
        db.create_all()

    return app
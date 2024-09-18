from flask import Blueprint

from app.routes.events import events_bp

api = Blueprint('api', __name__)
api.register_blueprint(events_bp)  # Register events blueprint
from flask import Blueprint, request, jsonify
from app.models.events import Event
from app.database import db
from datetime import datetime

events_bp = Blueprint('events', __name__)

@events_bp.route('/', methods=['POST'])
def create_event():
    data = request.json
    new_event = Event(
        name=data['name'],
        description=data.get('description'),
        start_date=datetime.fromisoformat(data['start_date']),
        available_spots=data['available_spots']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify(new_event.to_dict()), 201

@events_bp.route('/', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events])

@events_bp.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event.to_dict())

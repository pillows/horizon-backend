from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.models.events import Event
from app.models.users import User
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
@cross_origin()
def get_events():
    events = Event.query.all()
    for event in events:
        event_query = Event.query.get(event.id)
        users_registered_for_event = User.query.filter_by(registed_for_event_id=event.id).all()
        available_spots = event_query.available_spots - len(users_registered_for_event)
        event.available_spots = available_spots
    response = jsonify([event.to_dict() for event in events])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@events_bp.route('/join', methods=['POST'])
def join_event():
    data = request.json
    user_join_event = User(
        name=data['name'],
        email=data['email'],
        registed_for_event_id=data['event_id']
    )
    db.session.add(user_join_event)
    db.session.commit()
    return jsonify(data)

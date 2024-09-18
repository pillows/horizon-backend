# import os
# from dotenv import load_dotenv
# from flask import Flask
# from flask_cors import CORS

# from app.database import db
# from app.routes.events import events_bp
# from app.config import DB_URI

# load_dotenv()

# app = Flask(__name__)
# CORS(app)
# # Config
# app.env = os.environ.get('ENV')
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

# db.init_app(app)

# app.register_blueprint(events_bp, url_prefix='/api/events')

# with app.app_context():
#     db.create_all()
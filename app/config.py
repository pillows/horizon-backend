import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables
HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("APPLICATION_PORT", "5000"))
DB_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///app.db")  # Default to SQLite if not set
SCHEMA = os.getenv("SCHEMA", "horizon")  # Default schema
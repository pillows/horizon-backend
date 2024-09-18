import os

from flask_cors import CORS
from app import app
CORS(app)
if __name__ == "__main__":
    host = os.getenv('HOST') or '127.0.0.1'
    port = os.getenv('PORT') or '4000'
    debug = os.getenv('DEBUG') == 'True'
    CORS(app)
    app.run(host=host,
            port=port,
            debug=debug)
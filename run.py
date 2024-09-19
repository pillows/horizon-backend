# import os

# from flask_cors import CORS
# from app import app
# CORS(app)
# if __name__ == "__main__":
#     host = os.getenv('HOST') or '0.0.0.0'
#     port = os.getenv('PORT') or '4000'
#     debug = os.getenv('DEBUG') == 'True'
#     CORS(app)
#     app.run(host=host,
#             port=port,
#             debug=debug)

import os

from flask_cors import CORS
from app import app
CORS(app)
if __name__ == '__main__':
    print("Starting Flask development server...")
    app.run(host=os.getenv('HOST', '0.0.0.0'), port=int(os.getenv('PORT', 4000)))
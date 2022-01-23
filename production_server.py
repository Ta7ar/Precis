from waitress import serve
import logging
import os
from server import app

if __name__ == '__main__':
    # Production Server
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.INFO)
    port = os.environ.get("PORT", 8080)
    serve(app,host='0.0.0.0', port=port)
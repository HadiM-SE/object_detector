#!/usr/bin/env python3
"""
WSGI entry point for the Apple Mug Detector application.
This file is used by gunicorn to serve the Flask application.
"""

from app import create_app

# Create the Flask application instance
application = create_app()
app = application  # Alias for gunicorn

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=10000)

#!/usr/bin/env python3
"""
WSGI entry point for the Apple Mug Detector application.
This file serves as the main entry point for both development and production.
"""

import os
from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)

#!/usr/bin/env python3
"""
Simple startup script for the Apple Mug Detector application.
"""

import os
import sys

print('=== STARTING APPLICATION ===')
print('Python path:', sys.path)
print('Current directory:', os.getcwd())
print('Files in directory:', os.listdir('.'))

from app import create_app

app = create_app()
port = int(os.environ.get('PORT', 10000))
print(f'Starting Flask app on port {port}')

app.run(host='0.0.0.0', port=port, debug=False, threaded=True)

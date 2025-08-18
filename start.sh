#!/bin/bash
echo "=== STARTING APPLICATION ==="
echo "Using Python: $(which python)"
echo "Current directory: $(pwd)"
echo "Starting Flask app..."
python wsgi.py

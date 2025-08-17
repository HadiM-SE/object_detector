#!/bin/bash
echo "Starting Apple Mug Detector..."
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Starting Flask application..."
python wsgi.py

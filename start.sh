#!/bin/bash
set -e
echo "=== STARTING APPLICATION ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Starting Flask app with run.py..."
exec python run.py

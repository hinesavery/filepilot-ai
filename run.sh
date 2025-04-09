#!/bin/bash
echo "🔧 Starting FilePilot AI..."

source venv/bin/activate
export FLASK_APP=app.py
flask run --port=5001

from flask import Blueprint, render_template, request, jsonify
from app.utils import load_model, detect_objects
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/detect', methods=['POST'])
def detect():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        temp_path = os.path.join('static', 'uploads', file.filename)
        os.makedirs(os.path.dirname(temp_path), exist_ok=True)
        file.save(temp_path)
        
        detections = detect_objects(temp_path)
        
        return jsonify({
            'success': True,
            'detections': detections
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/health')
def health():
    return jsonify({'status': 'healthy'})

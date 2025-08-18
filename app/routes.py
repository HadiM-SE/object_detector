from flask import Blueprint, render_template, request, jsonify
from app.utils import load_model, detect_objects
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'GET':
        return jsonify({'message': 'This endpoint requires a POST request with an image file'}), 405
    
    try:
        print("=== DETECT ENDPOINT CALLED ===")
        print(f"Request method: {request.method}")
        print(f"Files in request: {list(request.files.keys())}")
        
        if 'image' not in request.files:
            print("No image file found in request")
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        print(f"File received: {file.filename}")
        
        if file.filename == '':
            print("Empty filename")
            return jsonify({'error': 'No file selected'}), 400
        
        temp_path = os.path.join('static', 'uploads', file.filename)
        print(f"Saving to: {temp_path}")
        
        os.makedirs(os.path.dirname(temp_path), exist_ok=True)
        file.save(temp_path)
        print("File saved successfully")
        
        print("Loading model...")
        detections = detect_objects(temp_path)
        print(f"Detections completed: {len(detections)} objects found")
        
        return jsonify({
            'success': True,
            'detections': detections
        })
        
    except Exception as e:
        print(f"ERROR in detect endpoint: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': str(e)}), 500

@bp.route('/health')
def health():
    return jsonify({'status': 'healthy'})

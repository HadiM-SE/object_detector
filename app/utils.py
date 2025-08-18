from ultralytics import YOLO
import os

_model = None

def load_model():
    global _model
    try:
        if _model is None:
            print("Loading YOLO model...")
            print("=== DEBUGGING FILE SYSTEM ===")
            print(f"Current working directory: {os.getcwd()}")
            print(f"Contents of current directory: {os.listdir('.')}")
            
            # Check multiple possible model locations
            model_paths = [
                os.path.join('models', 'best.pt'),           # Original path
                'best.pt',                                   # Root directory
                os.path.join(os.path.dirname(__file__), '..', 'models', 'best.pt'),  # Relative from utils.py
                os.path.join('/opt/render/project/src', 'models', 'best.pt')         # Absolute on Render
            ]
            
            # Try to create models directory if it doesn't exist
            if not os.path.exists('models'):
                try:
                    os.makedirs('models', exist_ok=True)
                    print("Created models directory")
                except Exception as mkdir_err:
                    print(f"Could not create models directory: {mkdir_err}")
            else:
                print(f"Models directory exists, contents: {os.listdir('models')}")
            
            # Try each possible model path
            model_path = None
            for path in model_paths:
                print(f"Trying model path: {path}")
                if os.path.exists(path):
                    model_path = path
                    print(f"Found model at: {model_path}")
                    print(f"Model file size: {os.path.getsize(model_path)}")
                    break
            
            print("=== END DEBUGGING ===")
            
            # If no model found, try using the default YOLO model
            if model_path is None:
                print("Custom model not found, using default YOLOv8n model")
                _model = YOLO('yolov8n.pt')  # Use default YOLOv8 nano model
                print("Default model loaded successfully")
            else:
                print("Loading custom model...")
                _model = YOLO(model_path)
                print("Custom model loaded successfully")
        
        return _model
    except Exception as e:
        print(f"ERROR loading model: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        raise

def detect_objects(image_path):
    try:
        print(f"Starting object detection on: {image_path}")
        model = load_model()
        print("Model loaded, running prediction...")
        results = model.predict(image_path, conf=0.25)
        print(f"Prediction completed, processing results...")
        
        detections = []
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    conf = float(box.conf[0].cpu().numpy())
                    cls = int(box.cls[0].cpu().numpy())
                    class_name = model.names[cls]
                    
                    detection = {
                        'class': class_name,
                        'confidence': round(conf, 3),
                        'bbox': {
                            'x1': round(float(x1), 2),
                            'y1': round(float(y1), 2),
                            'x2': round(float(x2), 2),
                            'y2': round(float(y2), 2)
                        }
                    }
                    detections.append(detection)
        
        print(f"Detection completed: {len(detections)} objects found")
        return detections
        
    except Exception as e:
        print(f"ERROR in detect_objects: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        raise

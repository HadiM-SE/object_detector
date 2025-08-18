from ultralytics import YOLO
import os

_model = None

def load_model():
    global _model
    try:
        if _model is None:
            print("Loading YOLO model...")
            model_path = os.path.join('models', 'best.pt')
            print(f"Model path: {model_path}")
            print(f"Model file exists: {os.path.exists(model_path)}")
            _model = YOLO(model_path)
            print("Model loaded successfully")
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

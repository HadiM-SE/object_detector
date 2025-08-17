from ultralytics import YOLO
import os

_model = None

def load_model():
    global _model
    if _model is None:
        model_path = os.path.join('models', 'best.pt')
        _model = YOLO(model_path)
    return _model

def detect_objects(image_path):
    model = load_model()
    results = model.predict(image_path, conf=0.25)
    
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
    
    return detections

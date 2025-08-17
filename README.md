# Apple vs Mug Detection

A Flask web application that uses YOLOv8 to detect apples and mugs in uploaded images.

## Features

- Upload images through a clean web interface
- AI-powered object detection using YOLOv8
- Real-time detection results with confidence scores
- Responsive design

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open http://localhost:5000 in your browser

## Docker Deployment

### Quick Start:
```bash
# Make script executable
chmod +x run_docker_simple.sh

# Run with Docker
./run_docker_simple.sh
```

### Manual Docker Commands:
```bash
# Build image
docker build -f docker/Dockerfile -t apple-mug-detector .

# Run container
docker run -d --name apple-mug-app -p 5000:5000 \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/static:/app/static \
  -v $(pwd)/templates:/app/templates \
  apple-mug-detector
```

## API Endpoints

- `GET /` - Main application interface
- `POST /detect` - Upload image and get detections
- `GET /health` - Health check endpoint

## Requirements

- Python 3.9+
- Flask 2.3.3
- Ultralytics YOLOv8
- PyTorch
- OpenCV
- Gunicorn (for production)

## Deployment Options

### Docker (Local/Production):
- **Port**: 5000
- **Full control** - customize everything
- **Persistent storage** - files don't disappear
- **Production ready** - scalable deployment
- **Easy setup** - one command deployment

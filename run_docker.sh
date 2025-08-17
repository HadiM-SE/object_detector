#!/bin/bash

echo "Starting Apple vs Mug Detector"

if ! docker info > /dev/null 2>&1; then
    echo "Docker is not running. Please start Docker first."
    exit 1
fi

if [ ! -f "docker/Dockerfile" ]; then
    echo "Dockerfile not found at docker/Dockerfile"
    exit 1
fi

echo "Building Docker image..."
docker build -f docker/Dockerfile -t apple-mug-detector .

mkdir -p static/uploads

echo "Stopping existing container if any..."
docker stop apple-mug-app 2>/dev/null || true
docker rm apple-mug-app 2>/dev/null || true

echo "Starting container..."
docker run -d \
  --name apple-mug-app \
  -p 5000:5000 \
  -v $(pwd)/models:/app/models \
  -v $(pwd)/static:/app/static \
  -v $(pwd)/templates:/app/templates \
  apple-mug-detector

echo "Application running at http://localhost:5000"

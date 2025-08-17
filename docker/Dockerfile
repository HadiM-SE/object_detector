FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    libgthread-2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY app/ ./app/
COPY templates/ ./templates/
COPY static/ ./static/
COPY config.py .
COPY app.py .
COPY wsgi.py .

# Create uploads directory
RUN mkdir -p static/uploads

EXPOSE 10000

# Use gunicorn with explicit module:app reference
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers", "1", "--timeout", "120", "wsgi:app"]

# Developer Guide

## Local Development Setup

1. **Prerequisites**
   - Python 3.11+
   - Docker
   - GCP SDK
   - FFmpeg

2. **Environment Setup**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

3. **Configuration**
```bash
# Set GCP credentials
gcloud auth application-default login
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"
```

## Running Locally

```bash
# Start FastAPI server
uvicorn src.main:app --reload

# Build Docker image
docker build -t video-analyzer .

# Run container
docker run -p 8080:8080 video-analyzer
```

## Deployment

1. **GCP Setup**
```bash
# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable aiplatform.googleapis.com
gcloud services enable storage.googleapis.com
```

2. **Deploy to Cloud Run**
```bash
./deploy.sh
```

## Testing

```bash
# Run tests
pytest tests/

# Generate test coverage
pytest --cov=src tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a pull request

## Best Practices

- Follow PEP 8 style guide
- Write unit tests for new features
- Update documentation
- Use type hints
- Handle errors gracefully

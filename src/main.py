from fastapi import FastAPI
from google.cloud import storage, pubsub_v1
import datetime
import base64
import json

app = FastAPI(title="Video Deal Analyzer")
storage_client = storage.Client()
publisher = pubsub_v1.PublisherClient()

PROJECT_ID = "video-deal-analyzer"
TOPIC_NAME = "video-uploads"

@app.get("/analyze")
async def analyze_video(gs_url: str):
    """Endpoint to trigger video analysis"""
    return {"status": "Analysis queued", "gcs_uri": gs_url}

@app.post("/upload-url")
def generate_upload_url(filename: str):
    """Generate secure upload URL"""
    bucket = storage_client.bucket("video-deal-analyzer-uploads")
    blob = bucket.blob(filename)
    
    url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(minutes=15),
        method="PUT"
    )
    return {"upload_url": url}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "services": {
            "cloud_storage": True,
            "vertex_ai": True
        }
    }

@app.post("/process-video")
async def process_video(event: dict):
    """Pub/Sub push endpoint"""
    video_data = json.loads(base64.b64decode(event["message"]["data"]))
    print(f"Processing new video: {video_data['name']}")
    return {"status": "processing_started"}

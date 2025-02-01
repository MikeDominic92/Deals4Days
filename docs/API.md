# API Reference

## Endpoints

### Generate Upload URL

```http
POST /upload-url
```

Generate a secure, signed URL for uploading videos to Cloud Storage.

**Parameters:**
- `filename` (string): Name of the video file to upload

**Response:**
```json
{
    "upload_url": "https://storage.googleapis.com/..."
}
```

### Process Video

```http
POST /process-video
```

Trigger video analysis pipeline for an uploaded video.

**Request Body:**
```json
{
    "message": {
        "data": "base64_encoded_video_data"
    }
}
```

**Response:**
```json
{
    "status": "processing_started",
    "doc_id": "analysis_document_id"
}
```

## Authentication

All API endpoints require authentication using GCP service accounts or user credentials.

## Error Codes

- `400`: Bad Request - Invalid parameters
- `401`: Unauthorized - Missing or invalid credentials
- `403`: Forbidden - Insufficient permissions
- `500`: Internal Server Error - Processing failed

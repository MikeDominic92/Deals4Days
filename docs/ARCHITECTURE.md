# System Architecture

## Overview

The Video Deal Analyzer is built on a modern, cloud-native architecture leveraging Google Cloud Platform services for scalability, reliability, and performance.

## Core Components

### 1. FastAPI Backend
- Handles HTTP requests
- Generates signed URLs for secure uploads
- Manages video processing pipeline
- Integrates with GCP services

### 2. Cloud Storage
- Stores uploaded video files
- Triggers events on new uploads
- Provides secure access via signed URLs

### 3. Cloud Pub/Sub
- Handles asynchronous video processing
- Enables event-driven architecture
- Manages processing queue

### 4. Vertex AI
- Performs video content analysis
- Extracts metadata and insights
- Provides ML-based video understanding

### 5. Cloud Run
- Hosts the FastAPI application
- Auto-scales based on demand
- Provides serverless execution

## Data Flow

1. User requests upload URL
2. Frontend uploads video to Cloud Storage
3. Storage trigger notifies Pub/Sub
4. Cloud Run service processes video
5. Results stored in Firestore

## Security

- IAM roles for access control
- Signed URLs for secure uploads
- Service account authentication
- Encrypted data at rest and in transit

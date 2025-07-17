# Luxembourg - LLM Visualization Platform

A platform for visualizing and interacting with Large Language Models, featuring real-time token analysis, cognitive guardrails, and advanced safety mechanisms.


## Overview

This project provides an interactive visualization platform for Large Language Models that combines:

- **Backend API** (`llm-viz`): FastAPI-based service for model inference, token analysis, and safety assessment
- **Frontend Interface** (`cognitive-guardrails`): Angular-based web application for user interaction and visualization
- **Safety Features**: Integration with SafeNudge for content moderation

## Architecture

The platform consists of two main components:

### Backend (llm-viz)
- **Technology**: Python FastAPI
- **Port**: 8000
- **Features**:
  - LLM model serving (Llama-3.2-1B-Instruct)
  - Token probability analysis
  - Safety content filtering
  - Response modification and guardrails
  - RESTful API endpoints

### Frontend (cognitive-guardrails)
- **Technology**: Angular with Material Design
- **Port**: 80
- **Features**:
  - Interactive token visualization
  - Real-time probability distributions
  - User-friendly prompt interface
  - Safety alerts and warnings
  - Responsive design

## Key Features

- 🔍 **Token Analysis**: Real-time visualization of token probabilities and model predictions
- 🛡️ **Safety Guardrails**: Automated content moderation using state-of-the-art safety models
- 📊 **Interactive Visualizations**: Dynamic charts and graphs for model behavior analysis
- 🎯 **Cognitive Bias Detection**: Integration with SafeNudge for bias identification
- 🚀 **High Performance**: Optimized for large-scale model inference with GPU acceleration

## Installation & Deployment

### Prerequisites

- **Hugging Face Token**: Required for model access ([get token here](https://huggingface.co/settings/tokens))
- **Model Access**: Request permission for [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)

### Local Development

```bash
# Clone the repository
git clone https://github.com/abell5/luxembourg.git

# Change to the project directory
cd luxembourg

# Build and run the containers
make run
```

### Kubernetes Deployment

For production deployment on Kubernetes clusters:

```bash
# Deploy the application
kubectl apply -f kubernetes.yaml

# Check deployment status
kubectl get pods
kubectl get svc
```

The Kubernetes deployment includes:
- **Multi-container Pod**: Both frontend and backend in a single pod for efficient communication
- **Resource Management**: GPU allocation for ML workloads, optimized memory usage
- **Load Balancing**: HAProxy ingress with SSL termination
- **Rolling Updates**: Zero-downtime deployments

### Access Points

- **Local Development**: 
  - Frontend: `http://localhost:80`
  - Backend API: `http://localhost:8000`
  - API Documentation: `http://localhost:8000/docs`

- **Production**: 
  - Web Interface: `https://llm-viz.users.hsrn.nyu.edu`

## API Documentation

### Core Endpoints

- `POST /generate` - Generate text responses with token analysis
- `POST /modify` - Apply safety modifications to generated content
- `GET /docs` - Interactive API documentation (Swagger UI)

## Project Structure

```
luxembourg/
├── api/                    # Backend FastAPI application
│   ├── api.py             # Main API endpoints
│   ├── safenudge.py       # Cognitive bias detection
│   ├── wildguard_safenudge.py # Content safety filtering
│   └── artifacts/         # Pre-trained model artifacts
├── client/                # Frontend Angular application
│   ├── src/app/          # Angular components and services
│   ├── src/environments/ # Environment configurations
│   └── public/           # Static assets
├── examples/             # Usage examples and demos
├── kubernetes.yaml       # Kubernetes deployment configuration
├── Dockerfile           # Container build instructions
└── requirements.txt     # Python dependencies
```
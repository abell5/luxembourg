#!/bin/bash

# Start nginx in background
nginx &

# Start the FastAPI application
cd /src
fastapi run api/api.py --port 8000 --workers -1

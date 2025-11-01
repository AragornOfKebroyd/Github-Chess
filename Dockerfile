# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

COPY server/requirements.txt /app/requirements.txt

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install system dependencies required for CairoSVG
# Install system deps for CairoSVG
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libcairo2 \
        libcairo2-dev \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 \
        libffi-dev \
        shared-mime-info && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy all project files
COPY . .

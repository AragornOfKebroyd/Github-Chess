# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

COPY server/requirements.txt /app/requirements.txt

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy all project files
COPY . .

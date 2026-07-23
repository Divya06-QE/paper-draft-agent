# Use a lightweight Python base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install system deps (if you later need msal/graph, curl, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY src ./src
COPY azure.yaml ./azure.yaml
COPY README.md ./README.md

# Environment (override in Azure)
ENV FOUNDRY_PROJECT_ENDPOINT=""
ENV FOUNDRY_MODEL_NAME="gpt-4.1"

# Expose app port
EXPOSE 8000

# Run the Responses host
CMD ["python", "src/main_responses_host.py"]

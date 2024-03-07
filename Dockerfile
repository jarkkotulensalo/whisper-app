# Use the official Python image as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Whisper from GitHub
RUN pip install git+https://github.com/openai/whisper.git

# Copy the entire project folder into the container at /app
COPY . .

# Expose the ports for Streamlit and Whisper API
EXPOSE 8501 8000

# Command to run both Streamlit app and Whisper API
CMD ["sh", "-c", "streamlit run app.py & uvicorn fastapi_app:app --host 0.0.0.0 --port 8000"]
# Streamlit Whisper Transcription Demo

This is a Streamlit app that allows users to upload a WAV audio file, transcribe it using the Whisper API, and display the transcribed text.

## Running the App

To run the Streamlit app inside a Docker container, follow these steps:

1. **Build the Docker image**:

docker build -t whisper_streamlit_app .


Replace `my_streamlit_app` with the desired name for your Docker image.

2. **Run the Docker container**:

docker run -p 8501:8501 whisper_streamlit_app


This command maps port 8501 on your host machine to port 8501 inside the Docker container where Streamlit is running. Adjust the port numbers as needed if you're using a different port for Streamlit.

3. **Access the Streamlit app**:

Once the Docker container is running, you can access your Streamlit app by opening a web browser and navigating to [http://localhost:8501](http://localhost:8501).

## Requirements

- Docker
- WAV audio file(s) for transcription

## Additional Notes

- Make sure that your Whisper API is running and accessible within the Docker container at the specified URL (`http://localhost:8000/whisper` in the provided example). Adjust the URL accordingly if your Whisper API is running on a different port or endpoint.
- Adjust the Streamlit app code if necessary to match your Whisper API endpoint and any other configurations.


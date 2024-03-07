import streamlit as st
import requests
import sounddevice as sd
import wave
import subprocess

# Streamlit UI components
st.title('Whisper API Transcription Demo')
wav_file = st.file_uploader('Upload Audio File', type=['wav', 'm4a'])


# Function to record audio from the microphone
def record_audio(duration, filename):
    fs = 44100  # Sample rate
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    wave.write(filename, fs, recording)
    

def m4a_to_wav(input_file, output_file):
    command = ['ffmpeg', '-i', input_file, output_file]
    subprocess.run(command)


# Function to call the Whisper API
def transcribe_audio(wav_data):
    try:
        files = {'files': wav_data}
        response = requests.post('http://localhost:8000/whisper', files=files)
        if response.status_code == 200:
            return response.json()['results'][0]['transcription']
        else:
            return f'Error {response.status_code} occurred.'
    except Exception as e:
        return f'Error: {str(e)}'


# Handling user input
if wav_file is not None:
    if st.button('Transcribe'):
        # create a spinner while waiting for the API response
        with st.spinner('Transcribing...'):
            wav_data = wav_file.read()
            text = transcribe_audio(wav_data)
        st.write('Transcription:')
        st.write(text)

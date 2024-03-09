import streamlit as st
import requests
import sounddevice as sd
import wave
import subprocess


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


# Streamlit UI components
st.title('Locally hosted Whisper-3 Transcription Demo')

# load file
audio_file = st.file_uploader('Upload Audio File', type=['wav', 'm4a', 'mp3'])

# play uploaded audio file
if audio_file is not None:
    if st.button("Play audio"):
        st.audio(audio_file, format='audio/ogg/m4a/wav/mp3')

    # transcribe audio
    if st.button('Transcribe'):
        # create a spinner while waiting for the API response
        with st.spinner('Transcribing...'):
            wav_data = audio_file.read()
            text = transcribe_audio(wav_data)
        st.write('Transcription:')
        st.write(text)


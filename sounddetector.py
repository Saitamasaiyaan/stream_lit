import streamlit as st
import numpy as np
import tensorflow as tf
import soundfile as sf
from io import BytesIO
from scipy.io import wavfile

# Load your pre-trained model
model = tf.keras.models.load_model('animal_sound_model.h5')

# Define a function to process audio
def process_audio(audio_bytes):
    # Read the audio file
    audio_data, samplerate = sf.read(BytesIO(audio_bytes))
    # Resample or reshape as needed for your model
    # Here we're assuming the model expects 1D audio data and a fixed length
    audio_data = np.mean(audio_data, axis=1)  # Convert to mono if stereo
    audio_data = np.resize(audio_data, (1, 16000))  # Example size, adjust as needed
    return audio_data

# Define a function to predict sound
def predict_sound(audio_data):
    predictions = model.predict(audio_data)
    return np.argmax(predictions, axis=1)  # Adjust based on your model output

# Define the animal classes
animal_classes = ["Cat", "Dog", "Bird", "Cow"]  # Update based on your model

# Streamlit app
st.title("Animal Sound Detector")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    # Read the uploaded file
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format="audio/wav")

    # Process and predict
    audio_data = process_audio(audio_bytes)
    prediction = predict_sound(audio_data)

    # Show the result
    st.write(f"Detected sound: {animal_classes[prediction[0]]}")

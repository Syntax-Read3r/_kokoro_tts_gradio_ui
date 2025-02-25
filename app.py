import gradio as gr
import requests
import uuid
import os

# Kokoro-FastAPI URL
KOKORO_API_URL = "http://kokoro-fastapi:8880/v1/audio/speech"

# Default voice (modify as needed)
TTS_VOICE = "af_bella"

# Directory to store audio files
OUTPUT_DIR = "generated_audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def tts_kokoro(text):
    """Send text to Kokoro-FastAPI, save as a single audio file, and return a download link"""
    
    payload = {
        "model": "kokoro",
        "input": text,
        "voice": TTS_VOICE
    }

    response = requests.post(KOKORO_API_URL, json=payload)

    if response.status_code == 200:
        audio_filename = f"{OUTPUT_DIR}/{uuid.uuid4()}.wav"
        
        # Save the generated audio file
        with open(audio_filename, "wb") as f:
            f.write(response.content)

        return audio_filename, audio_filename  # Playback + Download

    return "Error generating audio.", None

# Gradio Interface
gr.Interface(
    fn=tts_kokoro,
    inputs=gr.Textbox(label="Enter Text for TTS"),
    outputs=[
        gr.Audio(label="Generated Speech"),  # Audio playback
        gr.File(label="Download Audio")  # File download
    ],
    title="Kokoro TTS - Downloadable Audio",
    description="Enter text, generate speech using Kokoro TTS, and download the full audio file."
).launch(server_name="0.0.0.0", server_port=7860)

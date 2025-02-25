import gradio as gr
import requests
import uuid
import os

# Kokoro-FastAPI URL
KOKORO_API_URL = "http://kokoro-fastapi:8880/v1/audio/speech"

# Available voices (modify if needed)
VOICES = ["af", "af_bella", "af_irulan", "af_nicole", "af_sarah", "af_sky", "am_adam", "am_michael", "am_gurney", "bf_emma", "bf_isabella", "bm_george", "bm_lewis"]

# Available output formats
FORMATS = ["wav", "mp3", "flac", "aac", "opus"]

# Directory to store audio files
OUTPUT_DIR = "generated_audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def tts_kokoro(text, voice, speed, audio_format):
    """Send text to Kokoro-FastAPI with selected settings, save as a single audio file, and return a download link"""
    
    payload = {
        "model": "kokoro",
        "input": text,
        "voice": voice,
        "speed": speed,
        "format": audio_format
    }

    try:
        response = requests.post(KOKORO_API_URL, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}", None

    if response.status_code == 200:
        audio_filename = f"{OUTPUT_DIR}/{uuid.uuid4()}.{audio_format}"
        
        # Save the generated audio file
        with open(audio_filename, "wb") as f:
            f.write(response.content)

        return audio_filename, audio_filename  # Playback + Download

    return "Error generating audio.", None

# Gradio Interface
gr.Interface(
    fn=tts_kokoro,
    inputs=[
        gr.Textbox(label="Enter Text for TTS"),
        gr.Dropdown(choices=VOICES, label="Select Voice", value="af_sky"),
        gr.Slider(minimum=0.5, maximum=2.0, step=0.1, label="Speech Speed", value=1.0),
        gr.Dropdown(choices=FORMATS, label="Output Format", value="wav")
    ],
    outputs=[
        gr.Audio(label="Generated Speech"),  # Audio playback
        gr.File(label="Download Audio")  # File download
    ],
    title="Kokoro TTS - Customizable Speech",
    description="Enter text, select a voice, adjust speed, choose output format, and generate speech.",
    theme="default",
    css=".gradio-container::after { content: 'syntaxRead3r'; position: absolute; top: 10px; right: 10px; font-size: 14px; color: gray; }"
).launch(server_name="0.0.0.0", server_port=7860)

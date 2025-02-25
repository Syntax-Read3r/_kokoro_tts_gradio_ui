# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir gradio requests

# Expose the port for Gradio
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]

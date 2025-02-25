# Kokoro TTS Gradio UI 🎧

A **Gradio-based web interface** for **Kokoro-FastAPI**, providing **customizable text-to-speech (TTS)** with features like **voice selection, speech speed control, and multiple audio formats**. This setup integrates **FastAPI** and **Docker** to run efficiently on both **CPU** and **GPU**.

---

## **🚀 Features**
✅ **Text-to-Speech (TTS) using Kokoro**  
✅ **Supports multiple voices**  
✅ **Adjustable speech speed**  
✅ **Choose from various audio formats (MP3, WAV, FLAC, etc.)**  
✅ **Dockerized for easy deployment**  
✅ **Supports NVIDIA GPU acceleration**  

---

## **📌 Prerequisites**
Before you begin, ensure you have the following installed:

- **Docker** ([Install Docker](https://docs.docker.com/get-docker/))
- **NVIDIA GPU with CUDA (optional but recommended)**
- **NVIDIA Container Toolkit** ([Setup Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html))
- **Python 3.9+** (only if running outside Docker)

---

## **💍 Installation & Setup**
Follow these steps to set up the project from scratch:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Syntax-Read3r/_kokoro_tts_gradio_ui.git
cd _kokoro_tts_gradio_ui
```

### **2️⃣ Ensure NVIDIA Container Toolkit is Installed (For GPU Users)**
If you have an **NVIDIA GPU**, make sure the **NVIDIA Container Toolkit** is installed:
```bash
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
```
✅ If the output shows your GPU, you're good to go!

If not, follow [this guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

---

### **3️⃣ Update Docker Configuration**
Modify the **Docker Daemon configuration** to use NVIDIA runtime:

```bash
sudo nano /etc/docker/daemon.json
```
Add the following lines:
```json
{
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}
```
Save and restart Docker:
```bash
sudo systemctl restart docker
```

---

### **4️⃣ Build & Run the Docker Containers**
Run the following command to **build and start the services**:
```bash
docker-compose up --build
```
This will:
- Start **Kokoro-FastAPI** (Text-to-Speech API)
- Start **Gradio UI** for interaction

If everything is working, you should see output similar to:
```
Running on http://0.0.0.0:7860
```
Open **http://localhost:7860** in your browser to use the interface.

---

## **🛠️ Troubleshooting**
### **GPU Not Detected in Docker?**
- Run:
  ```bash
  docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
  ```
- If it **fails**, ensure **NVIDIA Container Toolkit** is installed ([Guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)).

### **Corrupted Docker Layers?**
If you encounter **layer extraction errors**, clear the cache and rebuild:
```bash
docker system prune -a --volumes
docker-compose up --build
```

### **Port Already in Use?**
Ensure no other instance is running:
```bash
docker ps  # Check running containers
docker-compose down  # Stop all services
```

---

## **📚 Documentation & References**
- **FastAPI Integration Guide**: [Kokoro-FastAPI Integration](https://docs.openwebui.com/tutorials/text-to-speech/Kokoro-FastAPI-integration)
- **Gradio Documentation**: [Gradio](https://www.gradio.app/)

---

## **💜 License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **👨‍💻 Author & Contributions**
**Developed by: SyntaxRead3r**  
Contributions are welcome! Feel free to submit a **pull request** or open an **issue**.


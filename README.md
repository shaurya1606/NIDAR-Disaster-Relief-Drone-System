# Human Detection System with YOLOv8

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-latest-green)

A robust real-time human detection system using YOLOv8 and OpenCV, designed for surveillance and monitoring applications. The system supports multiple camera inputs, customizable audio alerts, and automated detection logging.

## 🚀 Features

- **Real-time Human Detection**: Utilizes YOLOv8 for accurate human detection
- **Multiple Camera Support**:
  - Laptop/USB Camera
  - IP Camera
  - Video File Processing
- **Customizable Audio Alerts**:
  - Multiple frequency options
  - Custom sound file support
  - Configurable cooldown periods
- **Modular Architecture**:
  - Camera management
  - Sound alerts
  - Detection processing
  - Display handling
- **Automated Detection Logging**:
  - Frame capture of detections
  - Timestamp logging
  - Detection confidence scoring

## 📋 Prerequisites

- Python 3.8 or higher
- OpenCV 4.8+
- CUDA-capable GPU (optional, for better performance)

### System Requirements

```bash
# Linux
sudo apt-get install libgl1-mesa-glx libglib2.0-0 libasound2-dev portaudio19-dev

# Windows
# Ensure Microsoft Visual C++ Build Tools is installed
```

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/human-detection-system.git
cd human-detection-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download YOLOv8 weights (automatic on first run) or manually:
```bash
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
```

## 🎮 Usage

1. Run the main application:
```bash
python main.py
```

2. Select your input source:
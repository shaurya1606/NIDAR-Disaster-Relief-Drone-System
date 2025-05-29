# Human Detection System with YOLOv8

![Python Versions](https://img.shields.io/badge/python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-latest-green)

A robust, real-time human detection system using YOLOv8 and OpenCV. Designed for surveillance and monitoring, it supports multiple camera sources, customizable audio alerts, and automated detection logging.

---

## 📑 Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Output](#output)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Features
- **Real-time Human Detection** using YOLOv8
- **Multiple Camera Support**: Laptop/USB, IP Camera
- **Customizable Audio Alerts** (beeps or custom sound file)
- **Automated Detection Logging** (frames, timestamps, confidence)
- **Modular, Extensible Architecture**

---

## 🏗️ Architecture

```
human-detection-system/
├── main.py                  # Main entry point
├── modules/                 # System Module Directory
│   ├──__init__.py           # Contain Core Components
│   ├── camera_manager.py    # Camera input & connection
│   ├── detector.py          # YOLOv8-based detection
│   ├── sound_manager.py     # Audio alerts
│   └── display_manager.py   # Display & frame saving
├── detected_frames/         # Saved detection frames
├── yolov8n.pt               # YOLOv8 weights
├── alert.mp3                # Custom alert sound (optional)
├── requirements.txt         # Python dependencies
├── .gitignore               # Files that are ignored
└── README.md                # Information about the model
```

---

## 📋 Prerequisites

- Python 3.8 or higher
- OpenCV 4.8+
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- CUDA-capable GPU (optional, for better performance)

### System Requirements

- **Linux**: `sudo apt-get install libgl1-mesa-glx libglib2.0-0 libasound2-dev portaudio19-dev`
- **Windows**: Ensure Microsoft Visual C++ Build Tools is installed

---

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shaurya1606/NIDAR-Disaster-Relief-Drone-System.git
   cd NIDAR-Disaster-Relief-Drone-System
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download YOLOv8 weights:**
   - Automatic on first run, or manually:
   ```bash
   wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
   ```

---

## 🎮 Usage

1. **Run the main application:**
   ```bash
   python main.py
   ```
2. **Select your input source:**
   - 1: Laptop/USB Camera
   - 2: IP Camera (enter the stream URL)
3. **Choose alert sound:**
   - 1: High Beep (2000Hz)
   - 2: Medium Beep (1000Hz)
   - 3: Low Beep (500Hz)
   - 4: Custom Sound File (`alert.mp3`)
4. **View detections in real time.**
   - Press `q` to quit.

---

## 🧩 Modules

- **modules/camera_manager.py**: Handles camera selection, connection, and reconnection logic.
- **modules/detector.py**: Loads YOLOv8 model, runs detection, and annotates frames.
- **modules/sound_manager.py**: Manages alert sound selection and playback (beep or custom mp3).
- **modules/display_manager.py**: Displays annotated frames, overlays info, saves detection frames.

---

## 📂 Output

- **detected_frames/**: Saved frames with detected humans (every Nth detection frame).
- **alert.mp3**: Custom alert sound (optional, ignored by git).
- **yolov8n.pt**: YOLOv8 model weights (ignored by git).

---

## 🛠️ Troubleshooting

- **No camera detected**: Check your device or IP camera URL.
- **No sound**: Ensure your system supports `winsound` (Windows) or `playsound` (cross-platform). For custom sounds, place `alert.mp3` in the root directory.
- **Model not found**: Ensure `yolov8n.pt` is present or let the app download it on first run.
- **Permission errors**: Run as administrator or check directory permissions.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.


"""
Configuration settings for the Human Detection System
"""
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DETECTED_FRAMES_DIR = PROJECT_ROOT / "detected_frames"
MODEL_PATH = PROJECT_ROOT / "yolov8n.pt"
CUSTOM_SOUND_FILE = PROJECT_ROOT / "alert.mp3"

# Ensure required directories exist
DETECTED_FRAMES_DIR.mkdir(exist_ok=True)

# Detection settings
CONFIDENCE_THRESHOLD = 0.4
PERSON_CLASS_ID = 0

# Display settings
WINDOW_NAME = "Human Detection - YOLOv8n"
FRAME_SAVE_INTERVAL = 10
INFO_COLOR = (255, 0, 0)  # BGR format
DETECTION_COLOR = (0, 255, 0)  # BGR format

# Sound settings
SOUND_FREQUENCIES = {
    "high": 2000,
    "medium": 1000,
    "low": 500
}
SOUND_DURATION = 500  # milliseconds
SOUND_COOLDOWN = 3  # seconds

# Camera settings
RECONNECTION_ATTEMPTS = 3
RECONNECTION_DELAY = 2  # seconds

# Logging settings
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL 
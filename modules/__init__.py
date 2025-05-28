"""
Human Detection System Modules

This package contains the core components of the Human Detection System:
- CameraManager: Handles camera input and connection management
- SoundManager: Manages audio alerts and sound settings
- HumanDetector: Implements YOLOv8-based human detection
- DisplayManager: Handles video display and UI elements

Example usage:
    from modules.camera_manager import CameraManager
    from modules.sound_manager import SoundManager
    from modules.detector import HumanDetector
    from modules.display_manager import DisplayManager
"""

from .camera_manager import CameraManager
from .sound_manager import SoundManager
from .detector import HumanDetector
from .display_manager import DisplayManager
from modules import CameraManager, SoundManager

__version__ = '1.0.0'

__all__ = [
    'CameraManager',
    'SoundManager',
    'HumanDetector',
    'DisplayManager',
]

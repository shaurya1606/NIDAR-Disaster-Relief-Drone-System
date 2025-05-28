# tests/test_display_manager.py
import pytest
import os
from modules.display_manager import DisplayManager

def test_display_manager_init():
    dm = DisplayManager()
    assert os.path.exists("detected_frames")
    assert dm.frame_count == 0
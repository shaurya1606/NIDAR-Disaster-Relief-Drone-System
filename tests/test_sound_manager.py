# tests/test_sound_manager.py
import pytest
from modules.sound_manager import SoundManager

def test_sound_manager_init():
    sm = SoundManager()
    assert sm.SOUND_FREQUENCY == 2000
    assert sm.SOUND_DURATION == 500
    assert sm.SOUND_COOLDOWN == 3

def test_alert_type_display():
    sm = SoundManager()
    sm.SELECTED_SOUND = "1"
    assert sm.get_alert_type_display() == "High Beep (2000Hz)"
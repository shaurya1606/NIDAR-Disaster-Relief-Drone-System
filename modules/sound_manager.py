"""
Sound Management Module for Human Detection System
"""
import os
import threading
import winsound
from playsound import playsound

class SoundManager:
    def __init__(self):
        self.SOUND_FREQUENCY = 2000  # Hz (Higher frequency for better alerting)
        self.SOUND_DURATION = 500    # milliseconds
        self.SOUND_COOLDOWN = 3      # seconds between alerts
        self.last_sound_time = 0
        self.CUSTOM_SOUND_FILE = "alert.mp3"
        self.USE_CUSTOM_SOUND = True
        self.SELECTED_SOUND = None

    def setup_sound(self):
        """Configure sound settings based on user input"""
        print("\nAlert Sound Settings:")
        print("1. High Frequency Beep (2000 Hz)")
        print("2. Medium Frequency Beep (1000 Hz)")
        print("3. Low Frequency Beep (500 Hz)")
        print("4. Custom Sound File (alert.mp3)")
        
        sound_choice = input("Select alert sound (1-4): ").strip()
        self.SELECTED_SOUND = sound_choice

        if sound_choice == "1":
            self.SOUND_FREQUENCY = 2000
        elif sound_choice == "2":
            self.SOUND_FREQUENCY = 1000
        elif sound_choice == "3":
            self.SOUND_FREQUENCY = 500
        elif sound_choice == "4":
            if os.path.exists(self.CUSTOM_SOUND_FILE):
                self.USE_CUSTOM_SOUND = True
                print(f"Using custom sound file: {self.CUSTOM_SOUND_FILE}")
            else:
                print(f"⚠️ Custom sound file not found: {self.CUSTOM_SOUND_FILE}")
                print("Using default high frequency beep instead")
                self.SOUND_FREQUENCY = 2000
                self.SELECTED_SOUND = "1"

    def play_alert_sound(self):
        """Play the alert sound in a separate thread"""
        try:
            if self.SELECTED_SOUND == "4" and self.USE_CUSTOM_SOUND and os.path.exists(self.CUSTOM_SOUND_FILE):
                playsound(self.CUSTOM_SOUND_FILE)
            elif self.SELECTED_SOUND in ["1", "2", "3"]:
                winsound.Beep(self.SOUND_FREQUENCY, self.SOUND_DURATION)
        except Exception as e:
            print(f"⚠️ Could not play sound: {str(e)}")

    def play_alert_threaded(self):
        """Start sound playback in a separate thread"""
        threading.Thread(target=self.play_alert_sound, daemon=True).start()

    def get_alert_type_display(self):
        """Get the display text for current alert type"""
        return {
            "1": "High Beep (2000Hz)",
            "2": "Medium Beep (1000Hz)",
            "3": "Low Beep (500Hz)",
            "4": "Custom Sound"
        }.get(self.SELECTED_SOUND, "High Beep (2000Hz)") 
"""
Camera Management Module for Human Detection System
"""
import cv2
import time

class CameraManager:
    def __init__(self):
        self.cap = None
        self.camera_url = None
        self.source_type = None
        self.max_retries = 3
        self.retry_delay = 2

    def setup_camera(self):
        """Configure camera source based on user input"""
        print("\nSelect input source:")
        print("1. Laptop/USB Camera")
        print("2. IP Camera")
        choice = input("Enter choice (1-2): ").strip()

        if choice == "1":
            self.camera_url = 1
            self.source_type = "Laptop/USB Camera"
            print("Using laptop/USB camera")
        else:
            ip = input("Enter IP camera URL (e.g., http://172.18.18.53:4747/video): ").strip()
            self.camera_url = ip
            self.source_type = "IP Camera"
            print(f"Using IP camera at: {ip}")

    def connect(self):
        """Connect to the camera source with retries"""
        print("\nConnecting to camera...")
        
        for attempt in range(self.max_retries):
            if attempt > 0:
                print(f"Retrying connection (attempt {attempt + 1}/{self.max_retries})...")
                time.sleep(self.retry_delay)
            
            try:
                self.cap = cv2.VideoCapture(self.camera_url)
                
                if self.cap is None or not self.cap.isOpened():
                    print(f"❌ Failed to connect on attempt {attempt + 1}")
                    continue
                
                # Test read a frame to confirm connection
                ret, frame = self.cap.read()
                if not ret or frame is None:
                    print(f"❌ Could not read frame on attempt {attempt + 1}")
                    self.cap.release()
                    continue
                
                print("✅ Connected to camera successfully")
                return True
                
            except Exception as e:
                print(f"❌ Connection error on attempt {attempt + 1}: {str(e)}")
                if self.cap is not None:
                    self.cap.release()
                    self.cap = None
        
        raise ConnectionError("❌ Failed to connect to camera after all retries")

    def reconnect(self):
        """Attempt to reconnect to the camera"""
        print("\n⚠️ Connection lost. Attempting to reconnect...")
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        return self.connect()

    def read_frame(self):
        """Read a frame with error handling"""
        if self.cap is None:
            return False, None
            
        try:
            ret, frame = self.cap.read()
            if not ret or frame is None:
                return False, None
            return True, frame
        except Exception:
            return False, None

    def release(self):
        """Release the camera resources"""
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def get_source_text(self):
        """Get the display text for current camera source"""
        return self.source_type 
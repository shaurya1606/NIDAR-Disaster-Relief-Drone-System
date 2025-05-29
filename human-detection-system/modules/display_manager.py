"""
Display Management Module for Human Detection System
"""
import cv2
import time
import os
from datetime import datetime

class DisplayManager:
    def __init__(self, output_dir="detected_frames"):
        self.output_dir = output_dir
        self.prev_time = 0
        self.frame_count = 0
        self.save_interval = 10
        os.makedirs(output_dir, exist_ok=True)

    def add_fps(self, frame):
        """Add FPS counter to frame"""
        curr_time = time.time()
        fps = 1 / (curr_time - self.prev_time) if self.prev_time else 0
        self.prev_time = curr_time
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        return frame

    def add_info(self, frame, detections, source_text, alert_type):
        """Add detection info and other details to frame"""
        # Add detection count
        cv2.putText(frame, f"Detections: {detections}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        # Add source info
        cv2.putText(frame, f"Source: {source_text}", (10, 75),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        # Add alert type
        cv2.putText(frame, f"Alert: {alert_type}", (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        return frame

    def save_frame(self, frame, detections):
        """Save frame if there are detections (every Nth frame)"""
        if detections > 0 and self.frame_count % self.save_interval == 0:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.output_dir, f"detected_{timestamp}.jpg")
            cv2.imwrite(filename, frame)

        self.frame_count += 1

    def show_frame(self, frame):
        """Display the frame"""
        cv2.imshow("Human Detection - YOLOv8n", frame)

    def check_quit(self):
        """Check if user pressed 'q' to quit"""
        return cv2.waitKey(1) & 0xFF == ord('q') 
import cv2
from ultralytics import YOLO
import time
import os
import signal
from datetime import datetime

# Create output directory for detected frames
output_dir = "detected_frames"
os.makedirs(output_dir, exist_ok=True)

# Global variables for cleanup
cap = None
should_run = True

def signal_handler(signum, frame):
    """Handle cleanup when Ctrl+C is pressed"""
    global should_run
    print("\n👋 Caught interrupt signal. Cleaning up...")
    should_run = False

# Register the signal handler for Ctrl+C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

try:
    # Load YOLOv8n model
    print("Loading YOLO model...")
    model = YOLO('yolov8n.pt')
    print("✅ Model loaded successfully")

    # Laptop Camera stream URL (change this)
    camera_url = 0

    # IP Camera stream URL (change this)
    # camera_url = 'http://192.168.137.133:8080/video'  # <-- Replace with your IP!

    # Open the camera stream
    print("Connecting to IP camera...")
    cap = cv2.VideoCapture(camera_url)

    if not cap.isOpened():
        raise ConnectionError("❌ Could not open video stream")

    print("✅ Connected to IP camera")

    prev_time = 0
    frame_count = 0
    save_interval = 30  # Save every 30th frame with detection

    while should_run:
        try:
            ret, frame = cap.read()
            if not ret or frame is None:
                print("❌ Failed to read frame")
                # Try to reconnect
                cap.release()
                time.sleep(2)
                cap = cv2.VideoCapture(camera_url)
                continue

            # Check frame dimensions
            if frame.size == 0:
                print("❌ Empty frame received")
                continue

            # Inference
            results = model.predict(source=frame, conf=0.4, classes=[0], verbose=False)  # class 0 = person

            # Get the first result
            result = results[0]
            detections = 0

            # Draw boxes on frame
            if result.boxes is not None:
                for box in result.boxes:
                    cls_id = int(box.cls[0])
                    conf = box.conf[0]
                    if cls_id == 0:  # class 0 = person
                        detections += 1
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, f"Person {conf:.2f}", (x1, y1 - 10),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            # FPS calculation
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time else 0
            prev_time = curr_time
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 25),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            # Display
            cv2.imshow("Human Detection - YOLOv8n", frame)

            # Save frame if there are detections (every Nth frame)
            if detections > 0 and frame_count % save_interval == 0:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = os.path.join(output_dir, f"detected_{timestamp}.jpg")
                cv2.imwrite(filename, frame)

            frame_count += 1

            # Check for 'q' key press with a timeout
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print("👋 Exiting...")
                break

        except Exception as e:
            print(f"❌ Error processing frame: {str(e)}")
            continue

except KeyboardInterrupt:
    print("\n👋 Program interrupted by user")
except Exception as e:
    print(f"❌ Fatal error: {str(e)}")

finally:
    # Cleanup
    print("\n🧹 Performing cleanup...")
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()
    print("✅ Cleanup completed successfully")

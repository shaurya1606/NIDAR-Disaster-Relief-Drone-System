import cv2

# List available cameras
def list_cameras():
    available_cameras = []
    for i in range(10):  # Check first 10 indexes
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, _ = cap.read()
            if ret:
                available_cameras.append(i)
            cap.release()
    return available_cameras

# Print available cameras
cameras = list_cameras()
print(f"Available cameras at indexes: {cameras}")
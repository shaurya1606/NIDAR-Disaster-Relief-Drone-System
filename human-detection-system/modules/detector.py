"""
Human Detection Module using YOLOv8

This module provides human detection capabilities using the YOLOv8 model.
It handles model loading, inference, and visualization of detections.
"""
import cv2
import logging
from pathlib import Path
from ultralytics import YOLO

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HumanDetector:
    """
    Human detection class using YOLOv8.
    
    Attributes:
        model: YOLOv8 model instance
        conf_threshold: Confidence threshold for detections
        class_id: Class ID for person detection (0 in COCO dataset)
        model_path: Path to the YOLOv8 model weights
    """
    
    def __init__(self, model_path='yolov8n.pt', conf_threshold=0.4):
        """
        Initialize the detector.
        
        Args:
            model_path: Path to YOLOv8 weights file
            conf_threshold: Detection confidence threshold
        """
        self.model = None
        self.conf_threshold = conf_threshold
        self.class_id = 0  # person class in COCO dataset
        self.model_path = model_path

    def load_model(self):
        """
        Load the YOLOv8 model.
        
        Raises:
            FileNotFoundError: If model file doesn't exist
            RuntimeError: If model loading fails
        """
        try:
            if not Path(self.model_path).exists():
                logger.error(f"Model file not found: {self.model_path}")
                raise FileNotFoundError(f"Model file not found: {self.model_path}")
                
            logger.info("Loading YOLO model...")
            self.model = YOLO(self.model_path)
            logger.info("✅ Model loaded successfully")
            
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise RuntimeError(f"Failed to load model: {str(e)}")

    def detect_humans(self, frame):
        """
        Detect humans in a frame.
        
        Args:
            frame: Input image frame (numpy array)
            
        Returns:
            tuple: (processed_frame, num_detections)
            
        Raises:
            ValueError: If frame is invalid
            RuntimeError: If model is not loaded
        """
        if frame is None or frame.size == 0:
            logger.warning("Invalid frame received")
            raise ValueError("Invalid frame received")
            
        if self.model is None:
            logger.error("Model not loaded")
            raise RuntimeError("Model not loaded. Call load_model() first")

        try:
            # Inference
            results = self.model.predict(
                source=frame,
                conf=self.conf_threshold,
                classes=[self.class_id],
                verbose=False
            )

            # Get the first result
            result = results[0]
            detections = 0

            # Draw boxes on frame
            if result.boxes is not None:
                for box in result.boxes:
                    cls_id = int(box.cls[0])
                    conf = box.conf[0]
                    if cls_id == self.class_id:
                        detections += 1
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        
                        # Draw bounding box
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        
                        # Add confidence label
                        label = f"Person {conf:.2f}"
                        label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                        label_y = y1 - 10 if y1 - 10 > label_size[1] else y1 + 10
                        cv2.putText(frame, label, (x1, label_y),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            if detections > 0:
                logger.debug(f"Detected {detections} humans in frame")
                
            return frame, detections
            
        except Exception as e:
            logger.error(f"Error during detection: {str(e)}")
            raise RuntimeError(f"Detection failed: {str(e)}")

    def get_model_info(self):
        """
        Get information about the loaded model.
        
        Returns:
            dict: Model information
        """
        return {
            'model_path': self.model_path,
            'confidence_threshold': self.conf_threshold,
            'is_loaded': self.model is not None
        } 
# tests/test_detector.py
import pytest
import numpy as np
from modules.detector import HumanDetector

def test_detector_init():
    """Test detector initialization with default values"""
    detector = HumanDetector()
    assert detector.conf_threshold == 0.4
    assert detector.class_id == 0
    assert detector.model_path == 'yolov8n.pt'
    assert detector.model is None

def test_detector_custom_init():
    """Test detector initialization with custom values"""
    detector = HumanDetector(model_path='custom.pt', conf_threshold=0.5)
    assert detector.conf_threshold == 0.5
    assert detector.model_path == 'custom.pt'

def test_invalid_frame():
    """Test detection with invalid frame"""
    detector = HumanDetector()
    with pytest.raises(ValueError, match="Invalid frame received"):
        detector.detect_humans(None)
        
    with pytest.raises(ValueError, match="Invalid frame received"):
        detector.detect_humans(np.array([]))

def test_model_not_loaded():
    """Test detection without loading model"""
    detector = HumanDetector()
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    with pytest.raises(RuntimeError, match="Model not loaded"):
        detector.detect_humans(frame)

def test_get_model_info():
    """Test model info retrieval"""
    detector = HumanDetector(model_path='test.pt', conf_threshold=0.6)
    info = detector.get_model_info()
    assert info['model_path'] == 'test.pt'
    assert info['confidence_threshold'] == 0.6
    assert info['is_loaded'] is False
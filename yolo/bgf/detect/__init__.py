# BGF-YOLO based on Ultralytics YOLOv8x 8.0.109 object detection model with same license, AGPL-3.0 license

from .predict import DetectionPredictor, predict
from .train import DetectionTrainer, train
from .val import DetectionValidator, val

__all__ = 'DetectionPredictor', 'predict', 'DetectionTrainer', 'train', 'DetectionValidator', 'val'

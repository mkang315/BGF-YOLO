# BGF-YOLO based on Ultralytics YOLOv8x 8.0.109 object detection model with same license, AGPL-3.0 license

__version__ = '1.0.0'

from ...hub import start
from ...yolo.engine.model import YOLO
from ...yolo.utils.checks import check_yolo as checks

__all__ = '__version__', 'YOLO', 'checks', 'start'  # allow simpler import

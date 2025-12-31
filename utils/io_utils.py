import cv2
import os
from datetime import datetime

def save_snapshot(frame, out_dir="snapshots"):
    os.makedirs(out_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(out_dir, f"snapshot_{ts}.jpg")
    cv2.imwrite(filename, frame)
    return filename

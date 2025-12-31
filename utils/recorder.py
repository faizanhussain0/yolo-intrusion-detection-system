# utils/recorder.py
import cv2
import time
import os
from pathlib import Path

def record_clip_from_camera(cap, duration_seconds=4, out_dir="clips", fps=20, codec="mp4v"):
    """
    Records `duration_seconds` from an already-open cv2.VideoCapture `cap`.
    Returns the saved file path.
    """
    os.makedirs(out_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    filename = Path(out_dir) / f"clip_{ts}.mp4"

    # Get frame size from capture
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*codec)  # mp4v is usually safe
    out = cv2.VideoWriter(str(filename), fourcc, fps, (width, height))

    start = time.time()
    while time.time() - start < duration_seconds:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        # small sleep to avoid busy loop (adjust to fps)
        time.sleep(max(0, 1.0 / fps))

    out.release()
    return str(filename)

from utils.recorder import record_clip_from_camera
from alerts.telegram_alerts import send_text, send_photo, send_video
import cv2
import time
from detectors.yolo_detector import YoloDetector
from utils.io_utils import save_snapshot

MODEL_NAME = "yolov8n.pt"
DEVICE = "cpu"
PERSON_CLASS_ID = 0
CONF_THRESHOLD = 0.35
IOU_THRESHOLD = 0.45
PERSISTENCE_FRAMES = 8
ALERT_COOLDOWN_SECONDS = 30

def draw_boxes(frame, detections):
    for d in detections:
        x1, y1, x2, y2 = map(int, d["box"])
        label = f"{d['label']} {d['conf']:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

def main():
    detector = YoloDetector(model_name=MODEL_NAME, device=DEVICE, classes=[PERSON_CLASS_ID])
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Unable to open webcam.")
        return

    detection_count = 0
    last_alert_time = 0

    print("Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.predict(frame, conf=CONF_THRESHOLD, iou=IOU_THRESHOLD)

        persons = [d for d in detections if d["label"].lower() == "person" or d["cls"] == PERSON_CLASS_ID]

        if len(persons) > 0:
            detection_count += 1
        else:
            detection_count = 0

        
        if detection_count >= PERSISTENCE_FRAMES and (time.time() - last_alert_time) > ALERT_COOLDOWN_SECONDS:
            filename = save_snapshot(frame)
            print(f"[ALERT] Person detected! Snapshot saved: {filename}")

            try:
                send_text("🚨 ALERT: Person detected by YOLO intrusion system.")

                ok_photo = send_photo(filename, caption="Intruder snapshot")
                print("Telegram photo sent." if ok_photo else "Warning: Telegram photo failed to send.")

                clip_path = record_clip_from_camera(cap, duration_seconds=4, out_dir="clips", fps=20)
                print("Saved clip:", clip_path)

                ok_clip = send_video(clip_path, caption="Intruder clip (4s)")
                print("Telegram video sent." if ok_clip else "Warning: Telegram video failed to send.")

            except Exception as e:
                print("Failed to send Telegram alert:", e)

            last_alert_time = time.time()
            detection_count = 0
        

        draw_boxes(frame, persons)
        cv2.imshow("YOLO Intrusion Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

from ultralytics import YOLO

class YoloDetector:
    def __init__(self, model_name="yolov8n.pt", device=None, classes=None):
        self.model = YOLO(model_name)
        self.device = device
        self.classes = classes

    def predict(self, frame, conf=0.3, iou=0.45):
        results = self.model.predict(source=frame, conf=conf, iou=iou, device=self.device, verbose=False)
        detections = []
        res = results[0]
        boxes = res.boxes
        if boxes is None:
            return detections
        for box in boxes:
            xyxy = box.xyxy[0].cpu().numpy()
            conf_score = float(box.conf[0])
            cls_id = int(box.cls[0])
            label = res.names.get(cls_id, str(cls_id))
            if self.classes and cls_id not in self.classes:
                continue
            detections.append({"box": xyxy, "conf": conf_score, "cls": cls_id, "label": label})
        return detections

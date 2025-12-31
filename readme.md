YOLO-Based Intrusion Detection & Alert System
 Project Overview
This project is a real-time intrusion detection system that uses YOLOv8 object detection to detect the presence of a person through a live camera feed.  
When a person is detected consistently, the system automatically captures evidence (image + video clip) and sends instant Telegram alerts.

The project focuses on AI-powered automation and real-world application of computer vision models, not on training deep learning models from scratch.

---

 Problem Statement
Traditional CCTV systems only record footage and require manual monitoring, which is inefficient and error-prone.  
This project solves that problem by providing:

- Automatic person detection  
- Real-time alerts  
- Evidence capture (snapshot + short video clip)  
- Minimal human intervention  

---

 Key Features
- Real-time person detection using YOLOv8
- Live webcam feed with bounding boxes
- Telegram alerts with:
  - Text notification
  - Intruder snapshot
  - Short video clip (4 seconds)
- Alert cooldown to avoid notification spam
- Modular and scalable project structure
- Runs efficiently on CPU (no GPU required)

---

How the System Works
1. Webcam captures live video frames  
2. Each frame is passed to a pre-trained YOLOv8 model  
3. The model detects objects and filters only the “person” class  
4. Detection must persist for multiple frames to reduce false alerts  
5. On confirmation:
   - Snapshot is saved
   - Short video clip is recorded
   - Telegram alert is sent with evidence  

---

Tech Stack & Tools Used

Programming Language
- Python 3

 Libraries & Frameworks
- Ultralytics YOLOv8 – object detection
- PyTorch – deep learning backend
- OpenCV – camera access and video processing
- NumPy – numerical operations on image arrays
- Requests – Telegram Bot API integration
- python-dotenv – secure environment variable handling

Model
- YOLOv8n (Nano) – lightweight and fast object detection model

---

Project Structure
yolo_intrusion/
│
├── main.py # Main intrusion detection logic
├── alerts/
│ └── telegram_alerts.py # Telegram alert integration
├── detectors/
│ └── yolo_detector.py # YOLO inference wrapper
├── utils/
│ ├── recorder.py # Video clip recording
│ └── io_utils.py # Snapshot saving utilities
├── snapshots/ # Captured images
├── clips/ # Recorded intruder videos
├── requirements.txt
├── readme.md
└── yolov8n.pt # Pre-trained YOLO model


---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv

Activate Environment
.venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt


Set Telegram Credentials
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id


Run the System
python main.py


# AI-Based Hand Gesture Mouse Control Using Computer Vision  

This project implements a **real-time AI-based hand gesture mouse control system** using **Python, MediaPipe, OpenCV, and PyAutoGUI**. The system allows users to control their computer's mouse cursor and perform actions (click, drag, copy, paste) using **hand gestures** captured via a webcam, enabling a **hands-free interaction experience**.  

---

## ✨ Features  
✅ Real-time hand tracking using **MediaPipe**  
✅ **Mouse cursor control** using the index finger tip  
✅ **Pinch gesture recognition** for single-click and drag operations  
✅ **Three-finger pinch gesture** for **Copy** action (Ctrl+C / Cmd+C)  
✅ **Three-finger spread gesture** for **Paste** action (Ctrl+V / Cmd+V)  
✅ Works across **Windows, macOS, and Linux**  

---

## 🖥️ Tech Stack  
- **Domain**: Artificial Intelligence, Computer Vision  
- **Programming Language**: Python  
- **Libraries Used**:
  - [OpenCV](https://opencv.org/) - For webcam input and image processing  
  - [MediaPipe](https://google.github.io/mediapipe/) - For real-time hand tracking  
  - [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) - For controlling mouse and keyboard actions  

---

## 📂 Project Structure  
```

AI-Based-Hand-Gesture-Mouse-Control-Using-Computer-Vision/
│
├── gesture\_utils.py      # Utility functions for gesture detection
├── gesture\_mouse.py      # Main file to run the gesture-controlled mouse
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore unnecessary files in Git
└── README.md             # Project documentation

````

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/ashaheem32/AI-Based-Hand-Gesture-Mouse-Control-Using-Computer-Vision.git
cd AI-Based-Hand-Gesture-Mouse-Control-Using-Computer-Vision
````

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate    # For macOS/Linux
venv\Scripts\activate       # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python gesture_mouse.py
```

Press **`q`** to exit the application.

---

## 🎮 Gesture Controls

| Gesture               | Action                 |
| --------------------- | ---------------------- |
| **Index Finger Move** | Move mouse cursor      |
| **Thumb-Index Pinch** | Click / Drag & Select  |
| **3-Finger Pinch**    | Copy (Ctrl+C / Cmd+C)  |
| **3-Finger Spread**   | Paste (Ctrl+V / Cmd+V) |

---

## 🛠 Troubleshooting

### 1. Camera Not Working (macOS)

If you see:

```
OpenCV: not authorized to capture video
```

* Go to **System Settings > Privacy & Security > Camera**
* Enable camera access for **Terminal or VS Code**

Alternatively, run OpenCV with AVFoundation backend:

```python
cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
```

---

### 2. Permissions for Copy/Paste (macOS)

If Copy/Paste doesn’t work on macOS, modify hotkeys in `gesture_utils.py`:

```python
pyautogui.hotkey("command", "c")  # macOS
pyautogui.hotkey("ctrl", "c")     # Windows/Linux
```

---

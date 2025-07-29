import cv2
import mediapipe as mp
import pyautogui
from utils.gesture_utils import detect_gesture

# === Initialize MediaPipe and Webcam ===
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# === State Tracking ===
state = {
    "click_down": False,
    "dragging": False,
    "pinch_start_time": 0,
    "copy_triggered": False,
    "paste_triggered": False
}

# === Gesture Thresholds ===
thresholds = {
    "pinch_threshold": 40,    # For drag/click
    "spread_threshold": 80,   # Ensure fingers apart for drag
    "pinch_copy": 30,         # Tighter pinch for copy
    "spread_paste": 90        # Wider spread for paste
}

print("Press 'q' to exit.")

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame.")
        break

    frame = cv2.flip(frame, 1)  # Mirror view
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract Landmarks
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Image coords
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            middle_x, middle_y = int(middle_tip.x * w), int(middle_tip.y * h)

            # Screen coords: Move cursor with index finger
            screen_x = int(index_tip.x * screen_w)
            screen_y = int(index_tip.y * screen_h)
            pyautogui.moveTo(screen_x, screen_y)

            # Visual feedback
            cv2.circle(frame, (thumb_x, thumb_y), 8, (0, 255, 0), cv2.FILLED)
            cv2.circle(frame, (index_x, index_y), 8, (0, 255, 0), cv2.FILLED)
            cv2.circle(frame, (middle_x, middle_y), 8, (0, 255, 0), cv2.FILLED)
            cv2.line(frame, (index_x, index_y), (thumb_x, thumb_y), (255, 0, 255), 2)

            # Gesture Detection
            state = detect_gesture(
                thumb=(thumb_x, thumb_y),
                index=(index_x, index_y),
                middle=(middle_x, middle_y),
                frame=frame,
                state=state,
                thresholds=thresholds
            )

    cv2.imshow("AI Hand Gesture Mouse Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

import math
import pyautogui
import cv2
import time

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def detect_gesture(thumb, index, middle, frame, state, thresholds):
    """
    Detect gestures (click, drag, copy, paste) and perform actions.
    """
    click_down = state["click_down"]
    dragging = state["dragging"]
    pinch_start_time = state["pinch_start_time"]
    copy_triggered = state["copy_triggered"]
    paste_triggered = state["paste_triggered"]

    pinch_threshold = thresholds["pinch_threshold"]
    spread_threshold = thresholds["spread_threshold"]
    pinch_copy = thresholds["pinch_copy"]
    spread_paste = thresholds["spread_paste"]

    # Distances
    dist_thumb_index = calculate_distance(thumb, index)
    dist_thumb_middle = calculate_distance(thumb, middle)
    dist_index_middle = calculate_distance(index, middle)

    # === 1. Drag/Select ===
    if dist_thumb_index < pinch_threshold and dist_thumb_middle > spread_threshold:
        if not click_down:
            click_down = True
            pinch_start_time = time.time()
        else:
            held_duration = time.time() - pinch_start_time
            if held_duration >= 3 and not dragging:
                dragging = True
                pyautogui.mouseDown()
                cv2.putText(frame, "Selecting...", (index[0] + 20, index[1] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                copy_triggered = False
                paste_triggered = False

    # === 2. Copy (3-finger pinch) ===
    elif (dist_thumb_index < pinch_copy and
          dist_thumb_middle < pinch_copy and
          dist_index_middle < pinch_copy):
        if not copy_triggered:
            pyautogui.hotkey("command", "c")  # "cntrl" for Mac
            cv2.putText(frame, "COPY", (index[0] + 40, index[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            copy_triggered = True
            click_down, dragging = False, False
        paste_triggered = False

    # === 3. Paste (3-finger spread) ===
    elif (dist_thumb_index < pinch_copy and
          dist_index_middle > spread_paste and
          dist_thumb_middle > spread_paste):
        if not paste_triggered:
            pyautogui.hotkey("command", "v")  # "cntrl" for windows
            cv2.putText(frame, "PASTE", (index[0] + 40, index[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            paste_triggered = True
            click_down, dragging = False, False
        copy_triggered = False

    # === 4. Single Click / Reset ===
    else:
        if click_down:
            if dragging:
                pyautogui.mouseUp()
            else:
                pyautogui.click()
            click_down, dragging = False, False
        copy_triggered, paste_triggered = False, False

    state.update({
        "click_down": click_down,
        "dragging": dragging,
        "pinch_start_time": pinch_start_time,
        "copy_triggered": copy_triggered,
        "paste_triggered": paste_triggered
    })
    return state

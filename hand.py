import mediapipe as mp
import cv2

hand_model = mp.solutions.hands
hand_model_drawing = mp.solutions.drawing_utils
webcam = cv2.VideoCapture(0)

with hand_model.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        control, frame = webcam.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)
        if result.multi_hand_landmarks:
            for hand_lankmark in result.multi_hand_landmarks:
                hand_model_drawing.draw_landmarks(frame, hand_lankmark, hand_model.HAND_CONNECTIONS)
        cv2.imshow("Hands", frame)
        if cv2.waitKey(10) == 27:
            break

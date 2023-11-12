import cv2

video = cv2.VideoCapture("video.mp4")

while True:
    control, frame = video.read()
    cv2.imshow("Frame", frame)
    if cv2.waitKey(10) == 27:
        break

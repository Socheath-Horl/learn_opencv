import cv2

face_detection = cv2.CascadeClassifier("face.xml")
eye_detection = cv2.CascadeClassifier("eye.xml")

face = cv2.imread("face.jpg")
gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
faceResult = face_detection.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faceResult:
    cv2.rectangle(face, (x, y), (x + w, y + h), (255, 0, 0), 3)
    eyeResult = eye_detection.detectMultiScale(gray, 3.1, 3)
    for (eye_x, eye_y, width, height) in eyeResult:
        cv2.rectangle(face, (eye_x, eye_y), (eye_x + width, eye_y + height), (0, 255, 0), 2)

cv2.imshow("Detection", face)
cv2.waitKey(0)


import cv2

filled = cv2.imread("background.jpg")
cv2.circle(filled, (80, 80), 50, (0, 255, 0),-1)
cv2.rectangle(filled, (400, 450), (450, 560), (0, 0, 255),-1)

cv2.imshow("Filled", filled)
cv2.waitKey(0)

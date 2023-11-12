import cv2

circle = cv2.imread("black.jpg")
cv2.circle(circle, (150, 150), 100, (0, 0, 255), 3)

cv2.imshow("Circle", circle)
cv2.waitKey(0)

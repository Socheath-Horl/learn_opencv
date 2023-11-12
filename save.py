import cv2

img1 = cv2.imread("background.jpg")
cv2.circle(img1, (80, 80), 50, (0, 255, 0),-1)
cv2.rectangle(img1, (400, 450), (450, 560), (0, 0, 255),-1)

cv2.imwrite("new_image.jpg", img1)

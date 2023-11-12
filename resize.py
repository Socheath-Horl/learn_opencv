import cv2

img = cv2.imread("img.jpg")
resizing = cv2.resize(img, (250, 390))

cv2.imshow("Orignal", img)
cv2.imshow("Resizing", resizing)
cv2.waitKey(0)
import cv2

original = cv2.imread("img.jpg")
cropping = original[14:240, 50:350]
resizing = cv2.resize(original, (200, 200))

cv2.imwrite("cropped.jpg", cropping)
cv2.imwrite("resizing.jpg", resizing)

import cv2

myResizingImage = cv2.imread("resizing.jpg")
new_image = myResizingImage.copy()

cv2.imshow("Original", myResizingImage)
cv2.imshow("Copy", new_image)
cv2.waitKey(0)

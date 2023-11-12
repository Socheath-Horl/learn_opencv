import cv2

cropping = cv2.imread("img.jpg")
cropped = cropping[60:360, 40:240]

cv2.imshow("Original", cropping)
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)

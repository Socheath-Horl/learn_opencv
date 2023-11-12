import cv2

img = cv2.imread("median.jpg")
median = cv2.medianBlur(img, 7)

cv2.imshow("Original", img)
cv2.imshow("Median", median)
cv2.waitKey(0)

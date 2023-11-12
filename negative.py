import cv2

img1 = cv2.imread("edge.jpg")
negative = cv2.bitwise_not(img1)

cv2.imshow("Org", img1)
cv2.imshow("Negative", negative)
cv2.waitKey(0)

import cv2

img = cv2.imread("edge.jpg", 0)
canny = cv2.Canny(img, 130, 155)

cv2.imshow("Original", img)
cv2.imshow("Canny", canny)
cv2.waitKey(0)

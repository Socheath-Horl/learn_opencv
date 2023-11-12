import cv2

img = cv2.imread("edge.jpg")
blur = cv2.GaussianBlur(img, (5, 5), 3)

cv2.imshow("Org", img)
cv2.imshow("Blur", blur)
cv2.waitKey(0)

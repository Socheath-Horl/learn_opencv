import cv2

img = cv2.imread("resizing.jpg")
width = 200
height = 200
center_point = (width / 2, height / 2)
rot = cv2.getRotationMatrix2D(center_point, -30, 1.0)
rotated = cv2.warpAffine(img, rot, (width, height))

cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

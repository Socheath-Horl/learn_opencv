import cv2

img = cv2.imread("resizing.jpg")
rot1 = cv2.rotate(img, cv2.ROTATE_180)
rot2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow("180", rot1)
cv2.imshow("90", rot2)
cv2.waitKey(0)

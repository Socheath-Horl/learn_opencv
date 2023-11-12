import cv2

black = cv2.imread("black.jpg")

cv2.line(black, (120, 50), (250, 150), (255, 0, 0),2)

cv2.imshow("Line", black)

cv2.waitKey(0)

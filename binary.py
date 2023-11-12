import cv2 as cv

lane = cv.imread("lane.jpg", 0)
thresh, binary = cv.threshold(lane, 125, 255, cv.THRESH_BINARY)
print(thresh)
print(lane.shape)
cv.imshow("Original", lane)
cv.imshow("Binary", binary)
cv.waitKey(0)

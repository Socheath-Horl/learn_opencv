import cv2

text = cv2.imread("img.jpg")
cv2.putText(text, "Hello", (250, 140), cv2.FONT_ITALIC, 2, (255, 0, 210), 3)

cv2.imshow("Text", text)
cv2.waitKey(0)

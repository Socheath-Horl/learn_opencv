import cv2
img = cv2.imread("img.jpg")
(blue, green, red) = img[125, 50]
print("Blue: ", blue, "Green: ", green, "Red: ", red)
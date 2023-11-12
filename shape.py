import cv2

image = cv2.imread("img.jpg")
height, width, channels = image.shape
print("The height:", height, "The width:", width, "The channels: ", channels)

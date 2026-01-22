import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Coding Image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, __ = image.shape

for loop in range (3):
    plt.imshow(image_rgb)
    plt.title(f"Image Dimensions: width = {str(width)}, height = {str(height)}")
    plt.show()
    height -= 1000
    width -= 1000
    image_rgb = cv2.resize(image_rgb, (width, height))
    
import cv2
import numpy as np


image = cv2.imread("runner.jpeg")

height, width, channels = image.shape


dx = float(input("Enter the shearing factor for the x-axis: "))


sheared_image = np.zeros_like(image)

for i in range(height):
    for j in range(width):
        x = i + dx * j  
        y = j          
        x = max(0, min(int(x), height - 1))
        y = max(0, min(int(y), width - 1))
        image[int(x), int(y)] = image[i, j]


cv2.imshow("Sheared Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

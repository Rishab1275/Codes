import cv2
import math
import numpy as np

# Read the image
image = cv2.imread("runner.jpeg")

# Get image dimensions
height, width, channels = image.shape

# Convert angle from degrees to radians
theta = float(input("Angle of rotation for image in degrees: "))
theta_rad = math.radians(theta)

# Calculate the center point for rotation
center_x = width / 2
center_y = height / 2

# Create an array to store the rotated image
rotated_image = np.zeros_like(image)

# Perform rotation pixel by pixel
for i in range(height):
    for j in range(width):
        # Translate to origin
        x = i - center_y
        y = j - center_x
        
        # Rotate
        x_new = x * math.cos(theta_rad) - y * math.sin(theta_rad)
        y_new = x * math.sin(theta_rad) + y * math.cos(theta_rad)
        
        # Translate back to original coordinate system and round
        x_new += center_y
        y_new += center_x
        x_new = int(round(x_new))
        y_new = int(round(y_new))
        
        # Check if the new coordinates are within bounds
        if 0 <= x_new < height and 0 <= y_new < width:
            rotated_image[x_new, y_new] = image[i, j]

# Display the rotated image
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

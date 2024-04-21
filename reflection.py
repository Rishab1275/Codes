import cv2

image = cv2.imread("runner.jpeg")

height, width, channel = image.shape

key = int(input("Enter 0 for reflection on x axis and 1 on y axis "))

for i in range(height):
    for j in range(width):
        if(key==1):
            x = -i
            y = j
            image[i,j] = image[x,y]
        elif(key==0):
            y = -j
            x = i
            image[i,j] = image[x,y]

    
cv2.imshow("Reflected image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


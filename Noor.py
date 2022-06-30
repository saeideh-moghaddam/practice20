import cv2
import numpy as np

image= np.arange(0, 65025 , 1, np.uint8)
img=np.reshape(image , (255 , 255))
height , width =img.shape

for i in range ( height ):
    for j in range(width):
        img[i,0:6500]= 255 - i
    
cv2.imwrite("black and White.png",img)
cv2.imshow("black & White" , img)
cv2.waitKey()
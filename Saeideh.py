import cv2
import numpy as np

image= np.arange(0, 90000, 1, np.uint8)
img=np.reshape(image , (300 , 300))
img[ : ]=250
a=0 
while(a<130):
    img[a+100:a+120 , 120:180]=0
    a=a+60
    img[120:160 , 100:120]=0
    img[180:220 , 180:200]=0
    img[120:140 , 180:200]=0
    img[200:220 , 100:120]=0


print(img)
cv2.imwrite("Saeideh.png",img)
cv2.imshow("Saeideh" , img) 
cv2.waitKey()
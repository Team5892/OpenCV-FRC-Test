import cv
import cv2
import numpy as np
from time import sleep

cv2.namedWindow("Win")
cv2.namedWindow("Win2")

while True:
    for t in range(0, 6):
        if t == 0:
            image = cv2.imread("/home/pi/sample_images/RBG.png", -1)
        elif t == 1:
            image = cv2.imread("/home/pi/sample_images/GBR.png", -1)
        elif t == 2:
            image = cv2.imread("/home/pi/sample_images/BRG.png", -1)
        elif t == 3:
            image = cv2.imread("/home/pi/sample_images/BGR.png", -1)
        elif t == 4:
            image = cv2.imread("/home/pi/sample_images/RGB.png", -1)
        elif t == 5:
            image = cv2.imread("/home/pi/sample_images/GRB.png", -1)

        image2 = cv2.cvtColor(image, cv2.COLOR_RGB2HLS, 0)

        thresh = cv2.inRange(image2, (30,30,100), (90,60,255))

        moments = cv.Moments(cv.fromarray(thresh),0)
        area = cv.GetCentralMoment(moments, 0, 0)

        x = cv.GetSpatialMoment(moments, 1, 0)/area
        y = cv.GetSpatialMoment(moments, 0, 1)/area
        
        #create an overlay to mark the center of the tracked object 
        overlay = cv.CreateImage(cv.GetSize(cv.fromarray(image)), 8, 3) 
                
        cv.Circle(cv.fromarray(image), (int(x), int(y)), 2, (255, 255, 255), 20) 
                
        print ((x/320)*2)-1
        
        cv2.imshow("Win", thresh)
        cv2.imshow("Win2", image)

        cv2.waitKey(700)

cv2.destroyWindow("Win")
cv2.destroyWindow("Win2")

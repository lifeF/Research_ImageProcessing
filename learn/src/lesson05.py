import numpy as np
import cv2
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'Kalana Dhanajaya',(10,500), font, 1,(255,255,255),1,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
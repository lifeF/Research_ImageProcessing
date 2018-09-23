import numpy as np
import cv2
# Load an color image in grayscale for code need to be  #imread(path , 0)
img = cv2.imread('../img/Image1.jpg')
print(img[12,4])
img[:,:,0]=0
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
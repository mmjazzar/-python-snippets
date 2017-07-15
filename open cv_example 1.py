import cv2
import numpy as np

img = cv2.imread('C:\\Users\\mmjaz\\Desktop\\OneDrive_3_7-3-2017\\Button\\images_190.jpeg')

img = cv2.imread('C:\\Users\\mmjaz\\Desktop\\OneDrive_3_7-3-2017\\OneDrive_4_7-3-2017\\pop up.jpg')

gray= cv2.imread('C:\\Users\\mmjaz\\Desktop\\OneDrive_3_7-3-2017\\OneDrive_4_7-3-2017\\pop up.jpg',0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()




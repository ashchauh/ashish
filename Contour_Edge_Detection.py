
import numpy as np
import cv2

img= cv2.imread(r'C:\Users\Ashish\Desktop\Test\Image_Black_Background.png')
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
thresh=cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
cv2.imshow("BINARY", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
_, contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2=img.copy()
index=-1
color= (255,0,255)
thickness=1
cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow("CONTOURS", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

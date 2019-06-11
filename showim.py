import cv2
import numpy as np

a= '/home/ubuntu/Desktop/1BW_1/107_mask.png'

im=cv2.imread(a)
print im.shape
y,x=im.shape[:2]
print im.shape[0]
# print (x) #col
# print (y) #row
x1=71
y1=54
# y1= 243 #row        
# x1= 804	#col
print im[y1,x1] #[row,col]
cropim=im[50:240,50:300,:] #[y1:y2,x1:x2,:]
# cv2.circle(im,(x1,y1),5,(128,128,128))

dt = cv2.resize(im,(384,288))
# cv2.imwrite('/home/ubuntu/Desktop/a4_0.png',dt)
cv2.imshow('anh',dt)
cv2.waitKey(0)
cv2.destroyAllWindows()
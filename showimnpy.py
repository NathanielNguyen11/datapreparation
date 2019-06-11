import cv2
import numpy as np

a= '/home/ubuntu/Desktop/1/A01.npy'

im=np.load(a)
y,x=im.shape[:2]
print (x) #col
print (y) #row
# y1= 243 #row        
# x1= 804	#col
# print im[y1,x1] #[row,col]
cropim=im[y/2:y,x/2:x,:] #[y1:y2,x1:x2,:]
# cv2.circle(im,(x1,y1),5,(128,128,128))
# cv2.imshow('anh',cropim)
cv2.imwrite('/home/ubuntu/Desktop/A4.png',cropim)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
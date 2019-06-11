import cv2
import numpy as np
import os 
import sys


# a= '/media/ubuntu/Quang/challenge/liver/CT/experi/train/1/image/19085edc.png'

# label_img=cv2.imread(a)
# print label_img.shape
# y,x=im.shape[:2]
# for i in range(label_img.shape[0]):

#     for j in range(label_img.shape[1]):
#     	if (label_img[i, j, 0] <= 5 and label_img[i, j, 1]<= 5 and label_img[i, j, 2] <= 5):
#                 label_img[i, j] = 0
#                 # white
#             # elif (label_img[i, j, 0] > 232 and label_img[i, j, 1] > 232 and label_img[i, j, 2] > 232):
#             #     label_processed[i, j] = 3
#             # elif (label_img[i, j, 0] == 0 and label_img[i, j, 1] == 128 and label_img[i, j, 2] == 0):
#             #     label_processed[i, j] = 2
#             # elif (label_img[i, j, 0] == 128 and label_img[i, j, 1] == 0 and label_img[i, j, 2] == 0):
#             #     label_processed[i, j] = 3
#             # elif (label_img[i, j, 0] == 0 and label_img[i, j, 1] == 128 and label_img[i, j, 2] == 128):
#             #     label_processed[i, j] = 4
#             # elif (label_img[i, j, 0] == 128 and label_img[i, j, 1] == 0 and label_img[i, j, 2] == 128):
#             #     label_processed[i, j] = 5
#             # elif (label_img[i, j, 0] == 128 and label_img[i, j, 1] == 128 and label_img[i, j, 2] == 128):
#             #     label_processed[i, j] = 6
#             # elif (label_img[i, j, 0] == 128 and label_img[i, j, 1] == 128 and label_img[i, j, 2] == 0):
#             #     label_processed[i, j] = 7
#             # elif (label_img[i, j, 0] == 0 and label_img[i, j, 1] == 0 and label_img[i, j, 2] == 64):
#             #     label_processed[i, j] = 8
#         else:
#             pass
# cv2.imwrite(os.path.join('/home/ubuntu/Desktop/1.png'),label_img) 
# # print (x) #col
# print (y) #row
# y1= 216	 #row        
# x1= 546	#col
# print im[y1,x1] #[row,col]
y1 =21
y =440
x1 =52
x =621
# cropim=im[y1:y,x1:x,:] #[y1:y2,x1:x2,:]
# cv2.circle(im,(x1,y1),5,(128,128,128))
im1 = cv2.imread('/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/image/1010sdc.png')
cv2.imshow('anh',im1)
# cv2.imwrite('/home/ubuntu/Desktop/1/571.png',cropim)
cv2.waitKey(0)
cv2.destroyAllWindows()
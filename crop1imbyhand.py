import cv2
import numpy as np
import os
import sys
 


def crop(imageor_path,imagelb_path,y1,y2,x1,x2,i):
    orimage = cv2.imread(imageor)
    lbimage = cv2.imread(imagelb)

    croped_orimage = orimage[y1:y2,x1:x2,:] 
    croped_lbimage = lbimage[y1:y2,x1:x2,:]
    
    data_path = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d'%i
    # os.makedirs(data_path,0777 )

    cv2.imwrite('%s/CA01.png'%(data_path),croped_orimage)
    cv2.imwrite('%s/CA01_0.png'%(data_path),croped_lbimage)

    

if __name__ == '__main__':
    imageor = "/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/RA10.png"
    imagelb = "/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A10.png"
    i=10
    x1 = 3130
    x2 = 10190
    y1 = 2300
    y2 = 7170
    crop(imageor,imagelb,y1,y2,x1,x2,i)
import cv2
import numpy as np
import os
import sys
 


def crop(imageor_path,y1,y2,x1,x2):
    orimage = np.load(imageor_path)

    croped_orimage = orimage[y1:y2,x1:x2,:] 

 
    data_path = '/home/ubuntu/Desktop'

    cv2.imwrite('%s/CA01.png'%(data_path),croped_orimage)

    

if __name__ == '__main__':
    imageor = "/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/01.npy"

    x1 = 3000	
    x2 = 6000
    y1 = 3000
    y2 = 6000
    crop(imageor,y1,y2,x1,x2)
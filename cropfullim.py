import cv2
import numpy as np
import os
import sys
 


def crop(imageor_path,y1,y2,x1,x2,i):
    orimage = np.load(imageor)

    croped_orimage = orimage[y1:y2,x1:x2,:] 
    
    data_path = '/home/ubuntu/Desktop/A%02d'%i
    if os.path.isdir(data_path) == True:

        cv2.imwrite('%s/CA01.png'%(data_path),croped_orimage)
    else:
        os.makedirs(data_path,0777 )
        cv2.imwrite('%s/CA01.png'%(data_path),croped_orimage)
    

if __name__ == '__main__':
    i=1
    imageor = "/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/01.npy"
    x1 = 4000
    x2 = 6000
    y1 = 4000
    y2 = 6000
    crop(imageor,y1,y2,x1,x2,i)
    print ('Cut nat Sum Mi Ta`')
import numpy as np
import os
import cv2
from PIL import Image
import argparse
import sys
import random
IN= '/home/ubuntu/models/research/slim/tranfer_learning_tutorial/trainingdata/train450/train_photos/benign'
# OT= '/home/ubuntu/models/research/slim/transfer_learning_tutorial/trainingdata/train/train_photos/2'


def convert_label(label_img,rootdir,out_name):
    label_img=cv2.imread(label_img)
    # label_processed=np.zeros((label_img.shape[0],label_img.shape[1]),dtype=np.uint8)
    a=0
    for i in range(label_img.shape[0]):

        for j in range(label_img.shape[1]):
                #black
            # if (label_img[i, j,0] >= 128 and label_img[i, j, 1] >= 0 and label_img[i, j, 2] >= 0):
            if label_img[i, j,0] - 20 <=0:
                label_img[i, j,0] = 0             
            else:
                label_img[i, j,0] = label_img[i, j,0] -20

            if label_img[i, j,1] - 20 <=0:
                label_img[i, j,1] = 0
            else:
                label_img[i, j,1] = label_img[i, j,1] -20

            if label_img[i, j,2] - 20 <=0:
                label_img[i, j,2] = 0
            else:
                label_img[i, j,2] = label_img[i, j,0] -20
    cv2.imwrite(os.path.join(rootdir, out_name + '_d.png'),label_img) 

def parse_arguments(argv):
	parser = argparse. ArgumentParser()

	parser.add_argument('--input_dir', type = str,default=IN, help='Directory with original label image')
	# parser.add_argument('--output_dir',type = str,default=OT, help='Directory with processed label image')

	return parser.parse_args(argv)

def main(args):

    a=0 
    rootdir= os.path.expanduser(args.input_dir)
    # subpath = os.path.expanduser(args.output_dir)
    # check = os.path.isdir(subpath)
    # images = os.listdir(rootdir)
    # if check !=True:
        # os.makedirs(subpath,0777)
    # else:
        # pass
    # os.makedirs(subpath,0777 )
    list_files = os.listdir(rootdir)
    number_files=len(list_files)
    
    for filename in os.listdir(rootdir):
        

        files = os.path.join(rootdir,filename)       
        filename = filename[:-4]
        convert_label(files, rootdir, '%s'%filename)

        a=a+1
        print ('success in image number/total images: %d/%d'%(a, number_files))     

if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
    

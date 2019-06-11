
import numpy as np
import os
import cv2
from PIL import Image
import argparse
import sys
import os


IN = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/image'
OT = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/image1'
def convert_label(label_img,output_folder,out_name):
    label_img=cv2.imread(label_img)
    label_processed=np.zeros((label_img.shape[0],label_img.shape[1]),dtype=np.uint8)
    a=0
    for i in range(label_img.shape[0]):

        for j in range(label_img.shape[1]):
                #black
            if (label_img[i, j, 0] < 15 and label_img[i, j, 1] < 15 and label_img[i, j, 2] == 15):
                label_img[i, j] = 0
                # white
            # elif (label_img[i, j, 0] > 1 and label_img[i, j, 1] > 1 and label_img[i, j, 2] > 1):
            #     label_img[i, j] = 200
            # elif (label_img[i, j, 0] == 0 and label_img[i, j, 1] == 128 and label_img[i, j, 2] == 0):
            #     label_processed[i, j] = 2
            # elif (label_img[i, j, 0] == 128 and label_img[i, j, 1] == 0 and label_img[i, j, 2] == 0):
            #     label_processed[i, j] = 3
            # elif (label_img[i, j, 0] == 0 and label_img[i, j, 1] == 128 and label_img[i, j, 2] == 128):
            #     label_processed[i, j] = 4
            # elif (label_img[i, j, 0] == 128 and label_img[i, j, 1] == 0 and label_img[i, j, 2] == 128):
            #     label_processed[i, j] = 5
            # elif (label_img[i, j, 0] == 128 and label_img[i, j, 1] == 128 and label_img[i, j, 2] == 128):
            #     label_processed[i, j] = 6
            # elif (label_img[i, j, 0] == 128 and label_img[i, j, 1] == 128 and label_img[i, j, 2] == 0):
            #     label_processed[i, j] = 7
            # elif (label_img[i, j, 0] == 0 and label_img[i, j, 1] == 0 and label_img[i, j, 2] == 64):
            #     label_processed[i, j] = 8
            else:
                pass
    cv2.imwrite(os.path.join(output_folder, out_name + '.png'),label_img) 

def parse_arguments(argv):
	parser = argparse. ArgumentParser()

	parser.add_argument('--input_dir', type = str,default=IN, help='Directory with original label image')
	parser.add_argument('--output_dir',type = str,default=OT, help='Directory with processed label image')

	return parser.parse_args(argv)

def main(args):

    a=0 
    rootdir= os.path.expanduser(args.input_dir)
    subpath = os.path.expanduser(args.output_dir)
    check = os.path.isdir(args.output_dir)
    if check !=True:
        os.makedirs(subpath,0777)
    else:
        pass
    for filename in os.listdir(rootdir):
        list_files=os.listdir(rootdir)
        number_files=len(list_files)

        files = os.path.join(rootdir,filename)       
        filename = filename[:-4]
        convert_label(files, subpath, '%s'%filename)

        a=a+1
        print ('success in image number/total images: %d/%d'%(a, number_files))     

if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
    


import numpy as np
import os
import cv2
from PIL import Image
import sys
import argparse
# from skimage.io import imread, imsave

IN = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/LB'
OT = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/LB_1'


def convert_label(label_img,output_folder,out_name):
    label_img=cv2.imread(label_img)
    label_processed=np.zeros((label_img.shape[0],label_img.shape[1]),dtype=np.uint8)
    a=0
    for i in range(label_img.shape[0]):

        for j in range(label_img.shape[1]):
                #black
            if (label_img[i, j, 0] > 90 and label_img[i, j, 1] > 90 and label_img[i, j, 2] > 90):
                label_processed[i, j] = 1
                # Blue
            # elif (label_img[i, j, 0] == 1 and label_img[i, j, 1]== 1 and label_img[i, j, 2] == 1):
            #     label_processed[i, j] = 32
            #     #Green
            # elif (label_img[i, j, 0] == 2 and label_img[i, j, 1] == 2 and label_img[i, j, 2] == 2):
            #     label_processed[i, j] = 64
            #     #Red
            # elif (label_img[i, j, 0] == 3 and label_img[i, j, 1] == 3 and label_img[i, j, 2] == 3):
            #     label_processed[i, j] = 96
            # elif (label_img[i, j, 0] == 4 and label_img[i, j, 1] == 4 and label_img[i, j, 2] == 4):
            #     label_processed[i, j] = 128
            # elif (label_img[i, j, 0] == 5 and label_img[i, j, 1] == 5 and label_img[i, j, 2] == 5):
            #     label_processed[i, j] = 160
            # elif (label_img[i, j, 0] == 6 and label_img[i, j, 1] == 6 and label_img[i, j, 2] == 6):
            #     label_processed[i, j] = 188
            # elif (label_img[i, j, 0] == 7 and label_img[i, j, 1] == 7 and label_img[i, j, 2] == 7):
            #     label_processed[i, j] = 220
            # elif (label_img[i, j, 0] == 8 and label_img[i, j, 1] == 8 and label_img[i, j, 2] == 8):
            #     label_processed[i, j] = 252
            else:
                label_processed[i,j ] = 0
    cv2.imwrite(os.path.join(output_folder, out_name + '.png'),label_processed) 

def parse_arguments(argv):
    parser = argparse. ArgumentParser()

    parser.add_argument('--input_dir', type = str,default=IN, help='Directory with original label image')
    parser.add_argument('--output_dir',type = str,default=OT, help='Directory with processed label image')

    return parser.parse_args(argv)
def main(args): 
    a=0 
    rootdir= args.input_dir
    subpath = args.output_dir
    # subpath = outdir_lb
    if not os.path.isdir(subpath) :
        os.makedirs(subpath,0777)
    else:
        pass
    # os.makedirs(subpath,0777 )
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

    

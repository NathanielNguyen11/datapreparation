import numpy as np
import os
import cv2
from PIL import Image
import argparse
import sys
import os

IN = '/media/ubuntu/Quang/challenge/asshole/CVC-ColonDB/experi/1_1/2/test/image'
OT = '/media/ubuntu/Quang/challenge/asshole/CVC-ColonDB/experi/1_1/2/test/imagegr'
def convert_gray(im_path,out_path,out_name):
	print im_path
	image = cv2.imread(im_path,0)

	# gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	out_name = out_name+'.png'
	newpath = os.path.join(OT,out_name)
	cv2.imwrite(newpath,image)

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
    images = os.listdir(rootdir)
    if check !=True:
        os.makedirs(subpath,0777)
    else:
        pass

    number_files =  len(images)
    for image in os.listdir(rootdir):
    	name = image[:-4]
    	image =  os.path.join(rootdir,image)
        convert_gray(image,subpath,name)

        a=a+1
        print ('success in image number/total images: %d/%d'%(a, number_files))     

if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
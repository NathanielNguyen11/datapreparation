import numpy as np
import os
import cv2
from PIL import Image
import argparse
import sys


INDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/LB'
OTDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/LB_ero'
def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--input_dir',type = str,default=INDIR, help='Directory with original images.')
	parser.add_argument('--output_dir',type = str,default=OTDIR, help='Directory with original images.')
	# parser.add_argument('--time',type=int, help='How many time do you want to resize')
	return parser.parse_args(argv)
def main(args):
    a=0 
    rootdir= os.path.expanduser(args.input_dir)
    subpath = os.path.expanduser(args.output_dir)
    if not os.path.isdir(subpath):
    	os.makedirs(subpath,0777 )
    else:
    	pass
    for filename in os.listdir(rootdir):
		impath = os.path.join(rootdir,filename)
		img = cv2.imread(impath,0)
		print impath
		kernel = np.ones((15,15),np.uint8)
		erosion = cv2.erode(img,kernel,iterations = 1)
		# cv2.imshow('a',erosion)
		name = filename
		out_path = os.path.join(subpath,name)
		cv2.imwrite('%s'%out_path,erosion)

if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
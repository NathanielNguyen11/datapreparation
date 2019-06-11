import sys
import os
import argparse
import tensorflow as tf
import numpy as np
import random
from time import sleep
import cv2
import random
import argparse

IMDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/IM'
LBDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/LB_1'


def rotateim(image,label,name,imagenum):
	img = cv2.imread(image)
	label1 = cv2.imread(label)
	row = img.shape[0]
	col = img.shape[1]
	row1 = label1.shape[0]
	col1 = label1.shape[1]
	list1 = []

	# for k in range(360):
	#    f.append(k)

	for i in range(0,imagenum):
		a = random.randint(0,360)

		IM = cv2.getRotationMatrix2D((col/2,row/2),a,1)
		dst = cv2.warpAffine(img,IM,(col,row))
		cv2.imwrite(IMDIR+'/%s%03dr.png'%(name[:-4],a),dst)
		# print (os.path.dirname(image)+'/%s_%03d.png'%(name[:-4],a))

		IM1 = cv2.getRotationMatrix2D((col1/2,row1/2),a,1)
		dst1 = cv2.warpAffine(label1,IM1,(col1,row1))
		cv2.imwrite(LBDIR+'/%s%03dr.png'%(name[:-4],a),dst1)
			# print (os.path.dirname(label)+'/%s_%03d.png'%(name[:-4],a))


def main(args):

	rootdir= args.inputim_dir
	labeldir= args.inputlb_dir
	imagenum = 10
	file_name = os.listdir(rootdir)
	label_name = os.listdir(labeldir)
	# num_file=len(file_name)
	num_file =len(file_name)
	a = 0
	for filename in file_name:
		files = os.path.join(rootdir,filename)
		files2 = os.path.join(labeldir,filename)
		print (files2)
		rotateim(files,files2,filename,imagenum)
		a = a+1
		print ('%d/%d'%(a,num_file))

def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--inputim_dir',type = str,default =IMDIR ,help='Directory with original images.')
	parser.add_argument('--inputlb_dir',type = str,default = LBDIR ,help='Directory with label images.')
	# parser.add_argument('--time',type=int, help='How many time do you want to resize')
	return parser.parse_args(argv)

if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
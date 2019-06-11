
import sys
import os
import argparse
import tensorflow as tf
import numpy as np
import random
from time import sleep
import cv2
import random

def rotateim(image,name,imagenum):
	img = cv2.imread(image)
	row = img.shape[0]
	col = img.shape[1]
	f = []

	for i in range(0,imagenum):
		a = random.randint(0, 360)

		IM = cv2.getRotationMatrix2D((col/2,row/2),a,1)
		dst = cv2.warpAffine(img,IM,(col,row))
		cv2.imwrite(os.path.dirname(image)+'/%s_%04d.png'%(name[:-4],a),dst)
		# print (os.path.dirname(image)+'/%s_%03d.png'%(name[:-4],a))

		# IM1 = cv2.getRotationMatrix2D((col1/2,row1/2),a,1)
		# dst1 = cv2.warpAffine(label1,IM1,(col1,row1))
		# cv2.imwrite(os.path.dirname(label)+'/%s_%04d.png'%(name[:-4],a),dst1)
		# print (os.path.dirname(label)+'/%s_%03d.png'%(name[:-4],a))


def main():
	imagedir= '/home/ubuntu/models/research/slim/tranfer_learning_tutorial/trainingdata/train450/train_photos/malignant'
	# labeldir= '/home/ubuntu/Desktop/data/ashole/challenge/trainhd/train_1/2/label_1_1'
	imagenum = 6
	file_name = os.listdir(imagedir)
	# label_name = os.listdir(labeldir)
	num_file =len(file_name)
	a = 0
	for filename in file_name:
		files = os.path.join(imagedir,filename)
		# files2 = os.path.join(labeldir,filename)
		print (files)
		rotateim(files,filename,imagenum)
		a = a+1
		print ('%d/%d'%(a,num_file))

if __name__ == '__main__':
	main()
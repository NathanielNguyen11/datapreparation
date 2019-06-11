import Augmentor as aug
import numpy as np
import cv2
import os
import sys
import argparse

# im = '/home/ubuntu/Desktop/111/CVC-ClinicDB/Ground Truth/4.tif'

def rotateim(image,name):
	p = aug.Pipeline
	img = cv2.imread(image)
	row = img.shape[0]
	col = img.shape[1]

	for i in range (0,180):
		if i<=90:
			IM = cv2.getRotationMatrix2D((col/2,row/2),i,1)
			dst = cv2.warpAffine(img,IM,(col,row))
			cv2.imwrite(os.path.dirname(image)+'/%s_%03d.jpg'%(name[:-4],i),dst)
			print (os.path.dirname(image)+'/%s_%03d.jpg'%(name[:-4],i))
		if i>90:
			i= i+180
			IM = cv2.getRotationMatrix2D((col/2,row/2),i,1)
			dst = cv2.warpAffine(img,IM,(col,row))
			cv2.imwrite(os.path.dirname(image)+'/%s_%03d.jpg'%(name[:-4],i),dst)
			print (os.path.dirname(image)+'/%s_%03d.jpg'%(name[:-4],i))
def rotatelb(image,name):
	img = cv2.imread(image)
	row = img.shape[0]
	col = img.shape[1]

	for i in range (0,180):
		if i<=90:
			IM = cv2.getRotationMatrix2D((col/2,row/2),i,1)
			dst = cv2.warpAffine(img,IM,(col,row))
			cv2.imwrite(os.path.dirname(image)+'/%s_%03d.png'%(name[:-4],i),dst)
			print (os.path.dirname(image)+'/%s_%03d.png'%(name[:-4],i))
		if i>90:
			i= i+180
			IM = cv2.getRotationMatrix2D((col/2,row/2),i,1)
			dst = cv2.warpAffine(img,IM,(col,row))
			cv2.imwrite(os.path.dirname(image)+'/%s_%03d.png'%(name[:-4],i),dst)
			print (os.path.dirname(image)+'/%s_%03d.png'%(name[:-4],i))


def main():
	rootdir= '/home/ubuntu/Desktop/111/CVC-ClinicDB/1/'
	labeldir= '/home/ubuntu/Desktop/111/CVC-ClinicDB/2/'
	p = aug.Pipeline('/home/ubuntu/Desktop/111/CVC-ClinicDB/1')
	# p.ground_truth(labeldir)
	p.rotate(probability=1, max_left_rotation=5, max_right_rotation=5)
	p.flip_left_right(probability=0.5)
	p.zoom_random(probability=0.5, percentage_area=0.8)
	p.flip_top_bottom(probability=0.5)
	p.sample(20)
	# file_name = os.listdir(rootdir)
	# label_name = os.listdir(labeldir)
	# num_file=len(file_name)
	# for filename in file_name:
	# 	# files = os.path.join(rootdir,filename)
	# 	print (files)
	# 	rotateim(files,filename)
	# for labelname in label_name:
	# 	labels = os.path.join(labeldir,labelname)
	# 	print (labels)
	# 	rotatelb(labels,labelname)

if __name__ == '__main__':
	main()



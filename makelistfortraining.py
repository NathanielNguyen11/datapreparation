import os
import glob
import numpy as np
import argparse
import sys
from PIL import Image
import csv
import h5py
from os import listdir
from os.path import isfile, join
import pylab as plt
import matplotlib.image as mpimg
import colorsys
from PIL import Image

# def parse_args():
#     """Parse input arguments."""
#     parser = argparse.ArgumentParser(description='List all images in a folder.')
#     parser.add_argument('--dataset_folder', dest='dataset_folder', help='image dataset folder.', required=True,
#                         type=str)
#     parser.add_argument('--label_file', dest='label_file', help='image label file.', required=True,
#                         type=str)
#     parser.add_argument('--target_folder', dest='target_folder', help='image target_folder.', required=True,
#                         type=str)

#     args = parser.parse_args()

#     return args
def main():
	list_path='/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/list/'	
	os.makedirs(list_path,0777)	
	for i in range(1,11):
		# list_path='/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/list%02s/'%(i,i)

		image_folder='/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/image1'%i

		label_folder='/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/label2'%i

		list_im = os.listdir(image_folder)
		list_lb = os.listdir(label_folder)
		number_files = len (list_im)

		list_im_sorted= sorted(list_im)
		list_lb_sorted= sorted(list_lb)
	
		if (len(list_im)==len(list_lb) and os.path.isdir(image_folder) == True and os.path.isdir(label_folder) == True):

			f= open(os.path.join('%strain_list_A.txt'%(list_path)),'a')
			for entry_index in range(number_files):
				imagespath = os.path.join(image_folder,list_im_sorted[entry_index])
				labelspath = os.path.join(label_folder, list_lb_sorted[entry_index])
				f.write (imagespath + ' ' + labelspath +'\n')
		print ('success %d/10'%i)				
if __name__ == '__main__':
	main()
import os
import glob
import numpy as np
import argparse
import sys
from PIL import Image
import csv
from os import listdir
from os.path import isfile, join
import pylab as plt
import matplotlib.image as mpimg
import colorsys
from PIL import Image

IM = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/IM/'
LB = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/LB_1'
OT = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/list1/'
TYPE= 'train'
NUM='60'


def parse_arguments(argv):
	parser = argparse. ArgumentParser()

	parser.add_argument('--inputim_dir', type = str,default=IM, help='Directory with original label image')
	parser.add_argument('--inputlb_dir',type = str,default=LB,help='Directory with processed label image')
	parser.add_argument('--output_dir',type=str,default=OT,help='Directory with list')
	parser.add_argument('--type',type=str,default=TYPE,help='name of the list')
	parser.add_argument('--numdel',type=str,default=NUM,help='number of digits want to delete')
	return parser.parse_args(argv)

def main(args):
	list_path=os.path.expanduser(args.output_dir)
	name_list=os.path.expanduser(args.type)
	deldig = len(args.inputim_dir)+1
	print (deldig)
	if not os.path.isdir(list_path):
		os.makedirs(list_path,0777)
	else:
		pass
	image_folder=os.path.expanduser(args.inputim_dir)

	label_folder=os.path.expanduser(args.inputlb_dir)

	a = os.path.basename(args.inputim_dir)
	b = os.path.basename(args.inputlb_dir)
	print a ,b

	list_im = os.listdir(image_folder)
	list_lb = os.listdir(label_folder)
	number_files = len (list_im)

	list_im_sorted= sorted(list_im)
	list_lb_sorted= sorted(list_lb)
	print list_im_sorted
	if (len(list_im)==len(list_lb) and os.path.isdir(image_folder) == True and os.path.isdir(label_folder) == True):

		f= open(os.path.join('%s%s.txt'%(list_path,name_list)),'a')
		for entry_index in range(number_files):
			imagespath = os.path.join(a,list_im_sorted[entry_index][:-4])
			# labelspath = os.path.join(b, list_lb_sorted[entry_index][])
			# f.write (imagespath+' '+labelspath+'\n')
			f.write (imagespath+'\n')

if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))

# from scipy import misc
import sys
import os.path as paths
import os
import argparse
import tensorflow as tf
import numpy as np
import random
from time import sleep
import cv2


INDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train/'
OTDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1'
# TIME = 128
class ImageClass():
    "Stores the paths to images for a given class"
    def __init__(self, name, image_paths):
        self.name = name
        self.image_paths = image_paths
  
    def __str__(self):
        return self.name + ', ' + str(len(self.image_paths)) + ' images'
  
    def __len__(self):
        return len(self.image_paths)
def get_image_paths(facedir):
    image_paths = []
    if os.path.isdir(facedir):
        images = os.listdir(facedir)
        image_paths = [os.path.join(facedir,img) for img in images]
    return image_paths
def get_dataset(paths, has_class_directories=True):
    # dataset = []
    # paths1 = os.listdir(paths)
    # for path in paths1:
    path_exp = os.path.expanduser(paths)
    classes = os.listdir(path_exp)
    classes.sort()
    nrof_classes = len(classes)

    return classes,path_exp,nrof_classes


def main(args):
 	classes, path_exp,num_file= get_dataset(args.input_dir)
 	# n_time = args.time
 	# print (n_time)
	for file in range (0,num_file):
		facedir = path_exp+classes[file]
		print (facedir)

		filename = os.listdir(facedir)

		totalimage = len(os.listdir(facedir))
		os.makedirs('%s/%s/'%(args.output_dir,classes[file]),0777)
		for sort in range (0, totalimage):
			im_path = facedir+'/'+filename[sort]
			newname = filename[sort][:-4]
			print im_path
			img = cv2.imread(im_path)

			ba = cv2.resize(img,(300,300))
			cv2.imwrite('%s/%s/%s.png'%(args.output_dir,classes[file],newname),ba)



def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--input_dir',type = str,default=INDIR, help='Directory with original images.')
	parser.add_argument('--output_dir',type = str,default=OTDIR, help='Directory with original images.')
	# parser.add_argument('--time',type=int, help='How many time do you want to resize')
	return parser.parse_args(argv)

if __name__ == '__main__':

	main(parse_arguments(sys.argv[1:]))
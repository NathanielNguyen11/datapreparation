import tensorflow as tf
import tensorflow as tf
import numpy as np
import cv2
import os
import sys
import argparse
IMDIR = '/home/ubuntu/models/research/slim/tranfer_learning_tutorial/trainingdata/train450/train_photos/benign'
# LBDIR = '/home/ubuntu/Desktop/ashole_data/2/label'


def crop(imageor_path,crop_size_height,crop_size_weight,name):
    orimage = cv2.imread(imageor_path)
    folder = os.path.dirname(imageor_path)
    print folder
    # lbimage = cv2.imread(imagelb)
    heightcr = orimage.shape[1]/2
    print orimage.shape[1]
    weightcr = orimage.shape[0]/2
    # cv2.circle(orimage,(heightcr ,weightcr ), 2, (0,255,0), -1)

    y1 = weightcr - crop_size_weight/2
    y2 = weightcr + crop_size_weight/2
    x1 = heightcr - crop_size_height/2
    x2 = heightcr + crop_size_height/2
    print y1
    print x1
    croped_orimage = orimage[y1:y2,x1:x2,:]
    processed_im = cv2.resize(croped_orimage,(orimage.shape[1],orimage.shape[0]))
    # return processed_im
    newname = name+'_ct.png'
    cv2.imwrite('%s'%os.path.join(folder,newname),processed_im)

def main(args):
	images = os.listdir(IMDIR)
	height_crop = 300
	weight_crop = 300
	for image in images:
		image_path = os.path.join(IMDIR,image)
		# label_path = os.path.join(LBDIR,image)
		name = image[:-4]
		crop(image_path,height_crop,weight_crop,name)
		# crop(label_path,height_crop,weight_crop,name)
		print name

def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--inputim_dir',type = str,default=IMDIR ,help='Directory with original images.')
	# parser.add_argument('--inputlb_dir',type = str,default = LBDIR ,help='Directory with label images.')
	# parser.add_argument('--time',type=int, help='How many time do you want to resize')
	return parser.parse_args(argv)

if __name__ == '__main__':

	main(parse_arguments(sys.argv[1:]))
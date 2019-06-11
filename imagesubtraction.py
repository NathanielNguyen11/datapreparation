import numpy as np
import os
import cv2
from PIL import Image
import argparse
import sys

PREDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/Pre1'
LABELDIR ='/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/LB' 
IMDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/IM'
OUTIMDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/IM_SUB1'
OUTLBDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/LB_SUB2'
def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--pre_dir' ,type = str,default= PREDIR, help='Directory with original images.')
	parser.add_argument('--refer_dir' ,type = str,default= LABELDIR, help='Directory with original images.')
	parser.add_argument('--imtrain_dir' ,type = str,default= IMDIR, help='Directory with original images.')
	parser.add_argument('--processedim_dir' ,type = str,default= OUTIMDIR, help='Directory with original images.')
	parser.add_argument('--processedlb_dir' ,type = str,default= OUTLBDIR, help='Directory with original images.')
	return parser.parse_args(argv)
def image_subtract(label,pre,image_processed,out_name, outim_dir,outlb_dir):
	label = cv2.imread(label)
	pre = cv2.imread(pre)
	image_processed = cv2.imread(image_processed)
	out_name = out_name[:-4]+'s.png'
	outim_path = os.path.join( outim_dir, out_name)

	outlb_path = os.path.join( outlb_dir, out_name)

	diflabel_img = label - pre

	for i in range(pre.shape[0]):
		for j in range(pre.shape[1]):
			if (pre[i, j,0] == 255 and pre[i, j, 1] == 255 and pre[i, j, 2] == 255 and label[i, j,0] == 255 and label[i, j, 1] == 255 and label[i, j, 2] == 255):
				image_processed[i, j,0] = 0
				image_processed[i, j,1] = 0
				image_processed[i, j,2] = 0
	            # white

	        # 
			else:
				pass

	cv2.imwrite('%s'%outim_path,image_processed)
	cv2.imwrite('%s'%outlb_path,diflabel_img) 


def main(args):
	pre_dir = args.pre_dir
	label_dir = args.refer_dir
	process_dir = args.imtrain_dir
	outdir_im = args.processedim_dir
	outdir_lb = args.processedlb_dir

	index = 0

	if not os.path.isdir(outdir_lb) and not os.path.isdir(outdir_im):
		os.makedirs(outdir_im,0777)
		os.makedirs(outdir_lb,0777)
	else:
		pass

	list_preim = os.listdir(pre_dir)
	imnum = len(list_preim)
	for preim in list_preim:
		labelim_path = os.path.join(label_dir,preim)
		preim_path = os.path.join(pre_dir,preim)
		processim_path = os.path.join(process_dir,preim)
		print preim
		image_subtract(labelim_path,preim_path,processim_path,preim, outdir_im, outdir_lb)
		index = index +1
		print ('Processed : %d/%d'%(index, imnum))


if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))


# image_processed  = cv2.imread('/home/ubuntu/Desktop/data asshole/CVC-ClinicDB/data_for_train/Original1/141.png')
# image1 = cv2.imread("/home/ubuntu/Desktop/data asshole/CVC-ClinicDB/data_for_train/Ground Truth1/141.png")
# image2 = cv2.imread("/home/ubuntu/Desktop/CVC-612_1/2_pre_1/141.png")
# label_img = image1 - image2
# # print image3
# # print image3.shape
# # for i in range label_img.shape[0]:
# def main():
	

# cv2.imshow('image',image_processed)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
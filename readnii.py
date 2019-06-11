import numpy as np
import nibabel as nib
import cv2
import os
import sys
from nibabel.testing import data_path
import argparse

# img = nib.load('/media/ubuntu/Quang/challenge/liver/TUMOR/batch1/nas/01_Datasets/CT/LITS/Training Batch 1/volume-1.nii')

# example_ni1 = os.path.join(data_path, 'example4d.nii.gz')
INDIR ='/home/ubuntu/Desktop/pace/4' 
OTDIR ='/home/ubuntu/Desktop/pace/4_1'
def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--input_dir',type = str,default=INDIR, help='Directory with original images.')
	parser.add_argument('--output_dir',type = str,default=OTDIR, help='Directory with original images.')
	# parser.add_argument('--time',type=int, help='How many time do you want to resize')
	return parser.parse_args(argv)

def nii_read(nii_path,outfile,name):
	n1_img = nib.load(nii_path)
	data = n1_img.get_fdata()
	# array_img = np.array(img.dataobj)
	print  n1_img.shape[2]
	for i in range(n1_img.shape[2]):
		image = data[:,:,i]
		name = '%03d'%i+'.png'
		imout_path = os.path.join(outfile,name)
		cv2.imwrite(imout_path,image)
	# output_path = os.path.join(outfile,name)
	# cv2.imwrite('/home/ubuntu/Desktop/112123i1.png',data[:,:,120])

def main(args):
	input_dir = args.input_dir
	output_dir = args.output_dir
	imageniis = os.listdir(input_dir)
	if not os.path.isdir(output_dir):
		os.makedirs(output_dir,0777)
	else:
		pass
	for filename in os.listdir(input_dir):
		print filename
		nii_path = os.path.join(input_dir,filename)
		nii_read(nii_path,output_dir,filename)
        # list_files=os.listdir(rootdir)




if __name__ == '__main__':

	main(parse_arguments(sys.argv[1:]))
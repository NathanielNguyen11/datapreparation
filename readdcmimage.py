import numpy as np
import png
import pydicom
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

IM = '/media/ubuntu/Quang/challenge/Pancreas-CT/1/Pancreas-CT/PANCREAS_0001/1.2.826.0.1.3680043.2.1125.1.38381854871216336385978062044218957/1.2.826.0.1.3680043.2.1125.1.68878959984837726447916707551399667'
OT = '/media/ubuntu/Quang/challenge/Pancreas-CT/1/Pancreas-CT/PANCREAS_0001/1.2.826.0.1.3680043.2.1125.1.38381854871216336385978062044218957/1.2.826.0.1.3680043.2.1125.1.688789599848377264479167075513996671'


def parse_arguments(argv):
	parser = argparse. ArgumentParser()
	parser.add_argument('--inputim_dir', type = str,default=IM, help='Directory with original label image')
	parser.add_argument('--output_dir',type=str,default=OT,help='Directory with list')
	return parser.parse_args(argv)

def main(args):


	im_dir = args.inputim_dir
	out_dir = args.output_dir
	dcm_images = os.listdir(im_dir)
	im_num = len(dcm_images)
	a=0
	# path='/media/ubuntu/Quang/challenge/liver/CT_data_batch1/1/i0000,0000b.dcm'

	if not os.path.isdir(out_dir):
		os.makedirs(out_dir,0777)
	else:
		pass
		
	for image in dcm_images:

		path = os.path.join(im_dir,image)
		ds = pydicom.dcmread(path)

		shape = ds.pixel_array.shape

		# Convert to float to avoid overflow or underflow losses.
		image_2d = ds.pixel_array.astype(float)

		# Rescaling grey scale between 0-255
		image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0*3

		# Convert to uint
		image_2d_scaled = np.uint8(image_2d_scaled)

		# Write the PNG file
		name = image[:-4]+'.png'
		im_out = os.path.join(out_dir,name)
		with open(im_out, 'wb') as png_file:
		    w = png.Writer(shape[1], shape[0], greyscale=True)
		    w.write(png_file, image_2d_scaled)
		a=a+1
		print('converted: %d/%d '%(a,im_num))
if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
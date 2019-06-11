#find all your connected components (white blobs in your image)
import cv2
import numpy as np
import sys
import argparse
import os


IN = '/home/ubuntu/Desktop/3_seg/'
OT = '/home/ubuntu/Desktop/3_seg1/' 
SIZE = 450
def removesmall(image,size,out,name):
	img = cv2.imread(image,0)
	nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
	#connectedComponentswithStats yields every seperated component with information on each of them, such as size
	#the following part is just taking out the background which is also considered a component, but most of the time we don't want that.
	sizes = stats[1:, -1]; nb_components = nb_components - 1
	print nb_components
	# minimum size of particles we want to keep (number of pixels)
	#here, it's a fixed value, but you can set it as you want, eg the mean of the sizes or whatever

	min_size = size

	#your answer image
	img2 = np.zeros((output.shape))
	#for every component in the image, you keep it only if it's above min_size
	for i in range(0, nb_components):
	    if sizes[i] >= min_size:
	        img2[output == i + 1] = img[output == i + 1]

	    cv2.imwrite(out+'%s.png'%name,img2)
def parse_arguments(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_dir",default=IN,type=str,help="path to the input image")
	parser.add_argument("--output_dir",default=OT,type=str,help="path to the input image")
	parser.add_argument('--size' , default = SIZE,type = int , help = 'size condition')
	return parser.parse_args(argv)
def main(args):
	image_folder= args.input_dir
	image_out = args.output_dir
	outifle = os.path.isdir(image_out)
	if outifle ==False:
		os.makedirs(image_out,0777)
	else:
		pass
	files = os.listdir(image_folder)
	print files
	file_num = len(files)
	index = 0
	for image in files:
		image_path = image_folder + image
		name= image[:-4]
		print image_path
		removesmall(image_path,SIZE,image_out,name)
		index = index + 1
		print ('%d / %d '%(index, file_num))
if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))


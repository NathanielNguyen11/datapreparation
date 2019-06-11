import numpy as np
import os
import cv2
from PIL import Image
from skimage.io import imread, imsave
import shutil

def classify(image_label,image_im,black_path,blue_path,green_path,red_path,blackim_path,blueim_path,greenim_path,redim_path):
	label=cv2.imread(image_label,0)
	black_count =0
	blue_count =0 
	green_count =0
	red_count =0
	im_size= label.shape[0]*label.shape[1]
	for i in range(label.shape[0]):
		for j in range(label.shape[1]):
			# print (label[i,j])
			if label[i,j] == 0:	#black
				black_count	= black_count+1
			if label[i,j] ==1:	#blue
				blue_count = blue_count +1
			if label[i,j] ==2:	#green
				green_count = green_count+1
			if label[i,j] ==3:	#red
				red_count =red_count+1
	print('black : %d   blue: %d  green:%d  red:%d '%(black_count,blue_count,green_count,red_count))
	a=([black_count,blue_count,green_count,red_count])
	max_cell=np.amax(a)
	if max_cell== red_count:
		shutil.copy(image_label,red_path)
		shutil.copy(image_im,redim_path)
	if max_cell==black_count:
		shutil.copy(image_label,black_path)
		shutil.copy(image_im,blackim_path)
	if max_cell==blue_count:
		shutil.copy(image_label,blue_path)
		shutil.copy(image_im,blueim_path)
	if max_cell== green_count:
		shutil.copy(image_label,green_path)
		shutil.copy(image_im,greenim_path)

if __name__ == '__main__':
	
	numforder=10
	black = '/home/ubuntu/Desktop/datawsi/black/'
	blue = '/home/ubuntu/Desktop/datawsi/blue/'
	green = '/home/ubuntu/Desktop/datawsi/green/'
	red = '/home/ubuntu/Desktop/datawsi/red/'
	red_im = '/home/ubuntu/Desktop/datawsi/red_im/'
	black_im = '/home/ubuntu/Desktop/datawsi/black_im'
	blue_im = '/home/ubuntu/Desktop/datawsi/blue_im'
	green_im = '/home/ubuntu/Desktop/datawsi/green_im'
	os.makedirs(black,0777 )
	os.makedirs(blue ,0777 )
	os.makedirs(green,0777 )
	os.makedirs(red,0777 )
	os.makedirs(red_im,0777 )
	os.makedirs(black_im,0777 )
	os.makedirs(blue_im,0777 )
	os.makedirs(green_im,0777 )

	for i in range (1,numforder+1):
		label_path = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/label2/'%(i)
		im_path = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/image1/'%(i)

		print ('%s  \n'%label_path)
		print ('%s  \n'%im_path)
		allfile = os.listdir(label_path)
		totalfile= len(allfile)
		filetag=0

		for filename in os.listdir(label_path):
			filetag=filetag+1

			label_path1=label_path+filename
			im_name=filename[:-6]+'.png'
			im_path1 = im_path+im_name

			classify('%s'%label_path1,im_path1,black,blue,green,red,black_im,blue_im,green_im,red_im)
			print ('%d /total :%d'%(filetag	,totalfile))

		

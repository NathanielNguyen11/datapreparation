import numpy as np
import os
import cv2
from PIL import Image
import shutil

def classify(image_label,image_im,black_path,blue_path,green_path,red_path,blackim_path,blueim_path,greenim_path,redim_path):
	label=cv2.imread(image_label)
	black_count =0
	blue_count =0 
	green_count =0
	red_count =0
	im_size= label.shape[0]*label.shape[1]
	a=[]
	for i in xrange(0,label.shape[0],5):
		for j in xrange(0,label.shape[1],5):
			# print i
			# print j
			# print (label[i,j])
			# if label[i,j,0] == 0 and label[i,j,1]==0 and label[i,j,2]==0:	#black
			# 	black_count	= black_count+1
			if label[i,j,0] ==255 and label[i,j,1]==0 and label[i,j,2]==0:	#blue
				blue_count = blue_count +1
			if label[i,j,0] ==0 and label[i,j,1]==255 and label[i,j,2]==0:	#green
				green_count = green_count+1
			if label[i,j,0] ==0 and label[i,j,1] ==0 and label[i,j,2]==255:	#red
				red_count = red_count+1
	print('black : %d   blue: %d  green:%d  red:%d '%(black_count,blue_count,green_count,red_count))
	# a=([blue_count,green_count,red_count])
	a.__iadd__([blue_count])
	a.__iadd__([green_count])
	a.__iadd__([red_count])
	print a
	max_cell=np.amax(a)
	print max_cell
	if max_cell !=0:
		if max_cell== red_count :
			shutil.copy(image_label,red_path)
			print red_path
			shutil.copy(image_im,redim_path)
		if max_cell==blue_count :
			shutil.copy(image_label,blue_path)
			print blue_path
			shutil.copy(image_im,blueim_path)
		if max_cell== green_count :
			shutil.copy(image_label,green_path)
			print green_path
			shutil.copy(image_im,greenim_path)
	else:
		shutil.copy(image_label,black_path)
		print black_path
		shutil.copy(image_im,blackim_path)

if __name__ == '__main__':
	
    
	# numforder=10
	black = '/home/ubuntu/Desktop/1/black/'
	blue = '/home/ubuntu/Desktop/1/blue/'
	green = '/home/ubuntu/Desktop/1/green/'
	red = '/home/ubuntu/Desktop/1/red/'
	red_im = '/home/ubuntu/Desktop/1/red_im/'
	black_im = '/home/ubuntu/Desktop/1/black_im/'
	blue_im = '/home/ubuntu/Desktop/1/blue_im/'
	green_im = '/home/ubuntu/Desktop/1/green_im/'

	# os.makedirs(black,0777 )
	# os.makedirs(blue ,0777 )
	# os.makedirs(green,0777 )
	# os.makedirs(red,0777 )
	# os.makedirs(red_im,0777 )
	# os.makedirs(black_im,0777 )
	# os.makedirs(blue_im,0777 )
	# os.makedirs(green_im,0777 )
	label_path = '/home/ubuntu/Desktop/1/label1/'
	im_path = '/home/ubuntu/Desktop/1/image1/'
    
	# for i in range (1,numforder+1):

	# label_path = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/label1/'%(i)
	# im_path = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/image1/'%(i)


	print ('%s  \n'%label_path)
	print ('%s  \n'%im_path)
	allfile = os.listdir(label_path)
	totalfile= len(allfile)
	filetag=0

	for filename in os.listdir(label_path):
		filetag=filetag+1

		label_path1=label_path+filename
		print label_path1
		im_name=filename[:-4]+'.png'
		im_path1 = im_path+im_name

		classify('%s'%label_path1,im_path1,black,blue,green,red,black_im,blue_im,green_im,red_im)
		print ('%d /total :%d'%(filetag	,totalfile))

		

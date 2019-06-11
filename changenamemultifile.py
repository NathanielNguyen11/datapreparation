import numpy as np
import os
import cv2
import sys

# def copyremame(file_path,name,extend_name):



def main():
	rootdir = '/home/ubuntu/Desktop/data250_250/label/'
	files = os.listdir(rootdir)
	ext_name='_mask'
	for filename in files:
		
		newname = filename[:-4]
		a = rootdir + newname+'_mark.png'
		print a
            # copyremame(files, filename,ext_name)


if __name__ == '__main__':
	main()
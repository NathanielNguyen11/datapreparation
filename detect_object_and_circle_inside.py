# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np
import math
import random
import sys
import os


IM = '/media/ubuntu/Quang/challenge/asshole/hdtrain1/im'
LB = '/media/ubuntu/Quang/challenge/asshole/hdtrain1/gt'
# IM = '/home/ubuntu/Desktop/data/skin/skin_cancer/2017_test_1/image11'
# LB = '/home/ubuntu/Desktop/data/skin/skin_cancer/2017_test_1/label11'
# # construct the argument parse and parse the arguments
def parse_arguments(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument("--image",default=IM,type=str,help="path to the input image")
	parser.add_argument("--lb",default=LB,type=str,help="path to the output image")
	return parser.parse_args(argv)

def dist(p1,p2):
	# print p1
	distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
	return distance
def circle(lb,im,name):
	print lb
	print im
	image = cv2.imread(lb)
	image1 = cv2.imread(im)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

	# find contours in the thresholded image and initialize the
	# shape detector
	cnts = []
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	print len(cnts)
	dis = []
	if len(cnts) ==1:
		for c in cnts:
			# compute the center of the contour
			M = cv2.moments(c)
			if M["m00"]!= 0:
				cX = int(M["m10"] / M["m00"])
				cY = int(M["m01"] / M["m00"])
				# print c.shape[0]
				p2=[cX,cY]
				for i in range(0,c.shape[0]-1):
					a = c[i].tolist()
					b = a[0]
					# print b
					# print len(b)

					
					# print len(p2)
					k=dist(b,p2)

					dis.append(k)
					# print dis
					# print k
				radius = int(min(dis))
				print radius	
				r = random.randint(radius-2,radius)
				print r
				cv2.circle(image, (cX, cY), r, (0, 0, 0), -1)
				cv2.circle(image1,(cX, cY), r, (0, 0, 0), -1)
				x1 = cX - r
				x2 = cX + r
				y1 = cY - r
				y2 = cY + r

				print (x1,x2,y1,y2)
				for i in range(image1.shape[0]):
					for j in range(image1.shape[1]):
						# print ('i %d, j %d'%(i,j))
						point = [j,i]
						raim = dist(point,p2) 
						if raim <= r:
							if image1[i,j,0] == 0 and image1[i,j,1] == 0 and image1[i,j,2] == 0:
								ranvalue = random.randint(0,128)
								image1[i,j,0] = ranvalue
								image1[i,j,1] = ranvalue
								image1[i,j,2] = ranvalue
							else:
								pass
						else:
							pass


				dis = []
			else:
				pass
				# dis = []
		nameim = name+'o.jpg'
		lbpath= os.path.join(os.path.dirname(lb),nameim)
		impath= os.path.join(os.path.dirname(im),nameim)
		cv2.imwrite(lbpath,image)
		cv2.imwrite(impath,image1)
	else:
		pass

def main(args):
	a=0
	rootdir= os.path.expanduser(args.image)
	subpath = os.path.expanduser(args.lb)
	for filename in os.listdir(rootdir):
	    list_files=os.listdir(rootdir)
	    number_files=len(list_files)

	    file_im = os.path.join(rootdir,filename)
	    file_lb = os.path.join(subpath,filename)
	    print file_lb
	    filename = filename[:-4]
	    circle(file_lb, file_im , '%s'%filename)

		
if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
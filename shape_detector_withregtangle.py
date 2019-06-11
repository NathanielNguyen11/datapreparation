import argparse
import imutils
import cv2
import sys
import numpy as np
IM = '/home/ubuntu/Desktop/3_1.jpg'
# construct the argument parse and parse the arguments
def parse_arguments(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument("--image",default=IM,type=str,help="path to the input image")
	return parser.parse_args(argv)
	
def main(args):

	# load the image and resize it to a smaller factor so that
	# the shapes can be approximated better
	image = cv2.imread(args.image)
	resized = imutils.resize(image, width=300)
	ratio = image.shape[0] / float(resized.shape[0])

	# convert the resized image to grayscale, blur it slightly,
	# and threshold it
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

	# find contours in the thresholded image and initialize the
	# shape detector
	cnts = np.array([])
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)


	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	i=0
	# loop over the contours
	row= np.array([])
	col= np.array([])
	size=[]
	for c in cnts:
		
		# compute the center of the contour, then detect the name of the
		# shape using only the contour
		M = cv2.moments(c)
		cX = int((M["m10"] / M["m00"]) * ratio)
		cY = int((M["m01"] / M["m00"]) * ratio)

		c = c.astype("float")
		c *= ratio
		c = c.astype("int")

		x,y,w,h = cv2.boundingRect(c)
		print ('%s %s %s %s'%(x,y,w,h))

		cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

		cv2.imshow("Image", image)

		# show the output image

	cv2.imshow("Image", image)
	cv2.waitKey(0)
if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
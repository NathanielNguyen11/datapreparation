import argparse
import imutils
import cv2
import sys
import numpy as np
IM = '/home/ubuntu/Desktop/2_seg1/00000190.png'
# construct the argument parse and parse the arguments
def parse_arguments(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument("--image",default=IM,type=str,help="path to the input image")
	return parser.parse_args(argv)
def showbox(a,b):
	minrow = np.amin(a)
	maxrow = np.amax(a)
	mincol = np.amin(b)
	maxcol = np.amax(b)
	print minrow 
	print maxrow 
	print mincol
	print maxcol 
	return minrow,mincol,maxrow,maxcol
	
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

	mask = np.ones(image.shape[:2], dtype="uint8") 
	print cnts[1]
	# print cnts.shape
	# sd = ShapeDetector()
	i=0
	# loop over the contours
	row= np.array([])
	col= np.array([])
	for c in cnts:
		print c[0].shape
		
		b = cv2.arcLength(c[0],True)
		
		# compute the center of the contour, then detect the name of the
		# shape using only the contour
		M = cv2.moments(c)
		cX = int((M["m10"] / M["m00"]) * ratio)
		cY = int((M["m01"] / M["m00"]) * ratio)
		# shape = sd.detect(c)
		# print c[6]
		
		# multiply the contour (x, y)-coordinates by the resize ratio,
		# then draw the contours and the name of the shape on the image
		c = c.astype("float")
		c *= ratio
		c = c.astype("int")
		a = cv2.contourArea(c)
		print c.shape[0]
		print a

		if a>=700:
			cv2.drawContours(mask, [c], -1, 255, 2)

			cv2.putText(image,'%s'%i, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
				0.5, (255, 255, 255), 2)
			cv2.imshow("Image", mask)
			# show the output image
		else :
			cv2.drawContours(mask, [c], -1, 0, 15)
		image = cv2.bitwise_and(image, image, mask=mask)



	cv2.imshow("Image", image)
	cv2.imwrite('/home/ubuntu/Desktop/image.png',image)
	cv2.waitKey(0)
if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
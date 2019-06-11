import os
import argparse
import sys
import shutil


INPUTDIR1 = '/home/ubuntu/Desktop/2/'
INPUTDIR2 = '/home/ubuntu/Desktop/1/A9/' 

def main(args):
	strange = []
	fol1 = args.input1_dir
	fol2 = args.input2_dir
	files1 = os.listdir(fol1)

	for filename in files1:
		name = filename[:-13]
		copyim(name,fol2,filename)

def copyim(name, output,filename):
	file = INPUTDIR1+filename
	file2 = INPUTDIR2+filename
	if name == 'A09':
		shutil.move(file,file2)


def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--input1_dir',type = str,default = INPUTDIR1, help='Directory with original images.')
	parser.add_argument('--input2_dir',type = str,default = INPUTDIR2, help='How many time do you want to resize')
	
	return parser.parse_args(argv)
if __name__ == '__main__':

	main(parse_arguments(sys.argv[1:]))	
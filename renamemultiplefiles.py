import os
import argparse
import sys
import shutil

# INPUTDIR='/home/ubuntu/Desktop/Quang_dataset/image/6/'
INPUTDIR='/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300_train1/Pre'

def rename(folder):
	filenames = os.listdir(folder)
	# i=0
	# lsorted = sorted(filenames,key=lambda x: int(os.path.splitext(x)[0]))
	for filename in filenames:
		# print filename
		# shutil.move(os.path.join(folder,filename),'%07d'%i)
		i= filename[0:-15]
		print i
		os.rename(os.path.join(folder,filename),os.path.join(folder,'%s.png'%i))



def main(args):
	inputdir = args.input_dir
	# outputdir= args.output_dir
	rename(inputdir)

def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--input_dir',type = str,default = INPUTDIR, help='Directory with original images.')
	# parser.add_argument('--output_dir',type=str,default = OUTPUTDIR, help='How many time do you want to resize')
	
	return parser.parse_args(argv)
if __name__ == '__main__':

	main(parse_arguments(sys.argv[1:]))	
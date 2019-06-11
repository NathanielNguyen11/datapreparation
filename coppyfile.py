import os
import sys
import argparse
import shutil


INPUTDIR = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/LB_SUB'
INPUTDIR1= '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/IM_SUB'
OUTPUTDIR ='/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/label'
OUTPUTDIR1='/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/image'
def copy (file,input_path,output_path):
	file_path = input_path+'/'+file
	shutil.copy(file_path,output_path)

def main(args):
	input_dir= args.input_dir
	output_dir = args.output_dir
	filenames=os.listdir(input_dir)
	filenum = len(filenames)
	i=0

	for filename in filenames:
		i=i+1
		copy(filename,input_dir,output_dir)
		copy(filename,INPUTDIR1,OUTPUTDIR1)
		print ('success in image number/total images: %d/%d'%(i, filenum))



def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--input_dir',type = str,default = INPUTDIR, help='Directory with original images.')
	parser.add_argument('--output_dir',type=str,default = OUTPUTDIR, help='How many time do you want to resize')
	return parser.parse_args(argv)
if __name__ == '__main__':

	main(parse_arguments(sys.argv[1:]))	
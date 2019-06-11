import os
import sys
import argparse
import shutil


INPUTDIR = '/home/ubuntu/Desktop/data_need_prepare/2/JPEGImages/'
OUTPUTDIR ='/home/ubuntu/Desktop/data_need_prepare/2/image/'
FILEANO = '/home/ubuntu/Desktop/data_need_prepare/2/anotation/'
def copy (file,input_path,output_path):
	file_path = input_path+'/'+file+'.jpg'
	shutil.copy(file_path,output_path)

def main(args):
	input_dir= args.input_dir
	output_dir = args.output_dir
	filecon = FILEANO

	filenames=os.listdir(filecon)
	filenum = len(filenames)
	print filenum
	i=0
	for filename in filenames:
			# copy(filename,input_dir,output_dir)
		file = filename[:-4]
		copy(file, input_dir,output_dir)



def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--input_dir',type = str,default = INPUTDIR, help='Directory with original images.')
	parser.add_argument('--output_dir',type=str,default = OUTPUTDIR, help='How many time do you want to resize')
	return parser.parse_args(argv)
if __name__ == '__main__':

	main(parse_arguments(sys.argv[1:]))	
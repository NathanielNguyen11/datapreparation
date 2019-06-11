import os
import argparse
import sys
import shutil


INPUTDIR1 = '/media/ubuntu/Quang/challenge/liver/CT/experi/train/1/LB' #BIG
INPUTDIR2 = '/media/ubuntu/Quang/challenge/liver/CT/experi/train/1/IM' #SMALL

def main(args):
	strange = []
	fol1 = args.input1_dir #(BIG)
	fol2 = args.input2_dir #(Small)
	files1 = os.listdir(fol1)
	# filesname_1 = []
	# for filename1 in files1:
	# 	filesname_1.append(filename1[:-4])
	# filesname_1 = sorted(filesname_1)	 
	# print filesname_1

	files2 = os.listdir(fol2)
	# filesname_2 = []
	# for filename2 in files2:
	# 	filesname_2.append(filename2[:-4])
	# filesname_2 = sorted(filesname_2)
	# print filesname_2
	i=0
	a=0
	for filename2 in files2:
		if filename2 in files1:
			# print 1
			pass
		else:
			print filename2
			a=a+1
		i=i+1
		# print a



def parse_arguments(argv):
	parser = argparse.ArgumentParser()

	parser.add_argument('--input1_dir',type = str,default = INPUTDIR1, help='Directory with original images.')
	parser.add_argument('--input2_dir',type = str,default = INPUTDIR2, help='How many time do you want to resize')
	
	return parser.parse_args(argv)
if __name__ == '__main__':

	main(parse_arguments(sys.argv[1:]))	
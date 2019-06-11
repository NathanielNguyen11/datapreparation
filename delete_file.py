import os

image_dir = '/media/ubuntu/Quang/challenge/asshole/hdtrain1/1/1'
list_preim = os.listdir(image_dir)
imnum = len(list_preim)
for im in list_preim:
	print len(im)
	print im[:-4][:]
	# labelim_path = os.path.join(label_dir,preim)
	# os.remove("ChangedFile.csv")
import os


path = '/home/ubuntu/Desktop/1/'
# path1 = '/home/ubuntu/Desktop/1/'
files = os.listdir(path)

for file in files:
	name = file[:-9]+'_mask.jpg'
	print name
    os.rename(file,name)
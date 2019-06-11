import os
import copywithnamecon
import shutil

path = '/home/ubuntu/Desktop/data_need_prepare/1/JPEGImages/480p'
output_path = '/home/ubuntu/Desktop/data_need_prepare/1/JPEGImages'
path_con = '/home/ubuntu/Desktop/data_need_prepare/1/Annotations'
def rename(folder,name):
	filenames = os.listdir(folder)
	print filenames
	for filename in filenames:
		if filename[:-4]==name :
			file_path = folder +'/'+filename
			shutil.copy(file_path,output_path)
		# print addedname+'_'+filename
		# # shutil.move(os.path.join(folder,filename),'%07d'%i)
		# os.rename(os.path.join(folder,filename),os.path.join(folder,addedname+'_'+filename))
		# print (addedname+'_'+filename)
		# i= i+1

def main():

	files = os.listdir(path_con)
	images = []
	for file in files:
		# name = '/home/ubuntu/Desktop/1/'+ file[:-9]+'_mask.jpg'
		# os.rename(os.path.join(path,file),name)
		images.append(file)
	images = sorted(images)
	imchecker_num = len(images)

	namefol = []
	sub_files1 = os.listdir(path)
	for file in sub_files1:
		namefol.append(file)
	namefol = sorted (namefol)

	filenum = len(namefol)
	print filenum

	for i in range (filenum):
		subfol = path+'/'+ namefol[i]
		for j in range (imchecker_num):
			nameim = images[j][:-4]
			print subfol
			rename(subfol,nameim)

if __name__ == '__main__':
	main()

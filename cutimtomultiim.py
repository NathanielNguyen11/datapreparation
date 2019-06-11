import Image
import os
import glob
import cv2
# Set the root directory

def long_slice(image_path, out_name, outdir, sliceHeight, sliceWidth):
    img = cv2.imread(image_path) # Load image
    print img
    imageWidth = img.shape[1]
    imageHeight= img.shape[0] # Get image dimensions
    left = 0 # Set the left-most edge
    upper = 0 # Set the top-most edge
    b=1
    while (left+sliceWidth < imageWidth):
        while (upper+sliceHeight < imageHeight):

            working_slice = img[upper: upper + sliceHeight,left:left + sliceWidth] # Crop image based on created bounds
            # Save your new cropped image.
            cv2.imwrite(os.path.join(outdir, out_name + '_' + '%07d'%b + '.png'),working_slice)
            b=b+1
            upper += 50 # Incrementestt the horizontal position
            print (out_name + '_' + '%07d'%b + '.png')

        left += 50 # Increment the vertical position
        upper = 0
def long_slice1(image_path, out_name, outdir, sliceHeight, sliceWidth):
    img = cv2.imread(image_path) # Load image
    print img
    imageWidth = img.shape[1]
    imageHeight= img.shape[0] # Get image dimensions
    left = 0 # Set the left-most edge
    upper = 0 # Set the top-most edge
    a=1
    while (left+sliceWidth < imageWidth):
        while (upper+sliceHeight < imageHeight):

            working_slice = img[upper: upper + sliceHeight,left:left + sliceWidth] # Crop image based on created bounds
            # Save your new cropped image.
            cv2.imwrite(os.path.join(outdir, out_name + '_' + '%07d'%a + '.png'),working_slice)
            a=a+1
            upper += 50 # Incrementestt the horizontal position
            print (out_name + '_' + '%07d'%a + '.png')

        left += 50 # Increment the vertical position
        upper = 0        

if __name__ == '__main__':
    # Iterate through all the files in a set of directories.
    heightim = 600
    weightim = 600
    number_files=10
    for i in range (1,number_files+1):
        rootdir = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/image'%i
        subdir = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/image1'%i
        rootdir1 = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/label'%i
        subdir1 = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/label1'%i
        imfile=os.path.isfile(subdir)
        lbfile=os.path.isfile(subdir1)

        if imfile !=True and lbfile !=True:
        	os.makedirs(subdir,0777 )
        	os.makedirs(subdir1,0777 )
        for filename in os.listdir(rootdir):
            files = os.path.join(rootdir,filename)       
            filename = filename[:-4]
            long_slice(files, '%s'%filename, subdir, heightim , weightim)
            print ('success : total image')
        for filename1 in os.listdir(rootdir1):
            files1 = os.path.join(rootdir1,filename1)       
            filename1 = filename1[:-4]
            long_slice1(files1, '%s'%filename1, subdir1, heightim, weightim)
            print ('success : total label')

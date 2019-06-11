import Image
import os
import glob
# Set the root directory

def long_slice(image_path, out_name, outdir, sliceHeight, sliceWidth):
    img = Image.open(image_path) # Load image
    imageWidth, imageHeight = img.size # Get image dimensions
    left = 0 # Set the left-most edge
    upper = 0 # Set the top-most edge
    b=1
    while (left+sliceWidth < imageWidth):
        while (upper+sliceHeight < imageHeight):
            # If the bottom and right of the cropping box overruns the image.
            if (upper + sliceHeight > imageHeight and left + sliceWidth > imageWidth):
                bbox = (left, upper, imageWidth, imageHeight)
            # If the right of the cropping box overruns the image
            elif (left + sliceWidth > imageWidth):
                bbox = (left, upper, imageWidth, upper + sliceHeight)
            # If the bottom of the cropping box overruns the image
            elif (upper + sliceHeight > imageHeight):
                bbox = (left, upper, left + sliceWidth, imageHeight)
            # If the entire cropping box is inside the image,
            # proceed normally.
            else:
                bbox = (left, upper, left + sliceWidth, upper + sliceHeight)
            working_slice = img.crop(bbox) # Crop image based on created bounds
            # Save your new cropped image.
            working_slice.save(os.path.join(outdir, out_name + '_' + '%07d'%b + '.png'))
            b=b+1
            upper += 100 # Incrementestt the horizontal position
            print (out_name + '_' + '%07d'%b + '.png')
        left += 100 # Increment the vertical position
        upper = 0
def long_slice1(image_path1, out_name1, outdir1, sliceHeight1, sliceWidth1):
    img = Image.open(image_path1) # Load image
    imageWidth1, imageHeight1 = img.size # Get image dimensions
    left = 0 # Set the left-most edge
    upper = 0 # Set the top-most edge
    a=1
    while (left+sliceWidth1< imageWidth1):
        while (upper+sliceHeight1 < imageHeight1):
            # If the bottom and right of the cropping box overruns the image.
            if (upper + sliceHeight1 > imageHeight1 and left + sliceWidth1 > imageWidth1):
                bbox = (left, upper, imageWidth1, imageHeight1)
            # If the right of the cropping box overruns the image
            elif (left + sliceWidth1 > imageWidth1):
                bbox = (left, upper, imageWidth1, upper + sliceHeight1)
            # If the bottom of the cropping box overruns the image
            elif (upper + sliceHeight1 > imageHeight1):
                bbox = (left, upper, left + sliceWidth1, imageHeight1)
            # If the entire cropping box is inside the image,
            # proceed normally.
            else:
                bbox = (left, upper, left + sliceWidth1, upper + sliceHeight1)
            working_slice = img.crop(bbox) # Crop image based on created bounds
            # Save your new cropped image.
            working_slice.save(os.path.join(outdir1, out_name1 + '_' + '%07d'%a+'_0' + '.png'))
            a=a+1
            upper += 100 # Incrementestt the horizontal position
            print (out_name1 + '_' + '%07d'%a+'_0' + '.png')
        left += 100 # Increment the vertical position
        upper = 0
if __name__ == '__main__':
    # Iterate through all the files in a set of directories.
    heightim = 
    weightim =
    number_files=10
    for i in range (1,number_files+1):
        rootdir = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/image'%i
        subdir = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/image1'%i
        rootdir1 = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/label'%i
        subdir1 = '/home/ubuntu/ICIAR2018_BACH_Challenge/WSI/training_dataset/A%02d/label1'%i
        imfile=os.path.isfile(subdir)
        lbfile=os.path.isfile(subdir1)

        # if imfile !=True:
        # 	os.makedirs(subdir,0777 )
        # if not lbfile:
        # 	os.makedirs(subdir1,0777 )

        for filename in os.listdir(rootdir):
            files = os.path.join(rootdir,filename)       
            filename = filename[:-4]
            long_slice(files, '%s'%filename, subdir, heightim , weightim)
            print ('success : total image')
        for filename1 in os.listdir(rootdir1):
            files1 = os.path.join(rootdir1,filename1)       
            filename1 = filename1[:-6]
            long_slice1(files1, '%s'%filename1, subdir1, heightim, weightim)
            print ('success : total label')

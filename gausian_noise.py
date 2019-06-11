import cv2
import numpy as np
import argparse
import sys
import os
IN = '/home/ubuntu/Desktop/2'
SIG = 40
OT = '/home/ubuntu/Desktop/1_40' 
def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir',default= IN,type= str)
    parser.add_argument('--sigmal',default = SIG,type = int)
    parser.add_argument('--output_dir',default = OT,type = str)
    return parser.parse_args(argv)

def add_gaussian_noise(image_in, noise_sigma):
    image_in = cv2.imread(image_in)
    temp_image = np.float64(np.copy(image_in))

    h = temp_image.shape[0]
    w = temp_image.shape[1]
    noise = np.random.randn(h, w) * noise_sigma

    noisy_image = np.zeros(temp_image.shape, np.float64)
    if len(temp_image.shape) == 2:
        noisy_image = temp_image + noise
    else:
        noisy_image[:,:,0] = temp_image[:,:,0] + noise
        noisy_image[:,:,1] = temp_image[:,:,1] + noise
        noisy_image[:,:,2] = temp_image[:,:,2] + noise

    return noisy_image

def get_dataset (folder):
    sub_dirs = []
    im_path = []
    image_name = []
    files = os.listdir(folder)
    for file in files:
        sub_dirs.append(file)
    sub_dirs = sorted(sub_dirs)

    for subdir in sub_dirs:
        sub_path = os.path.join(folder,subdir)
        print sub_path
        images = os.listdir (sub_path)
        for image in images:
            image_path = os.path.join(sub_path,image)
            im_path.append(image_path)
            image_name.append(image)
            # print image_path
    image_name = sorted(image_name)
    im_path = sorted(im_path)
    return im_path, sub_dirs
# def save_noise_im (path, noisy_image):
#     cv2.imwrite(path, noisy_image)
def main(args):
    os.makedirs (args.output_dir,0777)
    input_fol = args.input_dir
    noisy_sigma = args.sigmal
    im_path, classes = get_dataset (args.input_dir)
    k_index = 0
    # print image_name
    for folder in range (0,len(classes)):
        subdir_new = OT+'/%s'%classes[folder]
        os.makedirs(subdir_new,0777)
        subdir = os.path.join(input_fol , classes[folder])
        images = os.listdir(subdir)
        # images= sorted(images)
        images.sort()
        print images
        path_exp = os.path.expanduser(subdir)
        print path_exp
        for image in images:
            image_link = os.path.join(subdir,image)
            noisy_image = add_gaussian_noise(image_link, noisy_sigma)
            image_name_new = subdir_new +'/%s'%image
            print image_name_new
            cv2.imwrite(image_name_new, noisy_image)
            # k_index = k_index + 1
    
if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))
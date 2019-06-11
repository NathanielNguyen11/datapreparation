import cv2
import numpy as np
import argparse
import sys
import os
import PIL
from PIL import Image

IN = '/home/ubuntu/Desktop/image_test/dataset'
RE_INDEX = 1.5
OT = '/home/ubuntu/Desktop/casia/CASIA-maxpy-clean' 
def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir',default= IN,type= str)
    parser.add_argument('--sigmal',default = RE_INDEX,type = int)
    parser.add_argument('--output_dir',default = OT,type = str)
    return parser.parse_args(argv)

def re_resolution(image_in, reso_index):
    orig= Image.open(image_in).convert("RGBA")
    im = Image.new("RGB", orig.size, "#ffffff")
    im.paste(orig, None, orig)
    return im

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
    # os.makedirs (args.output_dir,0777)
    output_dir = args.output_dir
    input_fol = args.input_dir
    re_index = args.sigmal
    im_path, classes = get_dataset (args.input_dir)
    k_index = 0
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
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
            reso_image = re_resolution(image_link, re_index)
            image_name_new = subdir_new +'/%s'%image
            print image_name_new
            w, h = reso_image.size
            reso_image.thumbnail((w * 160/106, h * 160/106), Image.ANTIALIAS)
            reso_image.save(image_name_new, quality=50,ssoptimize=True, progressive=True)
            # k_index = k_index + 1
    
if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))
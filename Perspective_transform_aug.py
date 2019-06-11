import tensorflow as tf
import numpy as np
import cv2
import os
import sys
import argparse

IMDIR = '/media/ubuntu/Quang/datset/Image'
LBDIR = '/media/ubuntu/Quang/datset/Label'


def get_mask_coord(imshape):
    vertices = np.array([[(0.09 * imshape[1], 0.99 * imshape[0]), 
                          (0.43 * imshape[1], 0.6 * imshape[0]), 
                          (0.56 * imshape[1], 0.6 * imshape[0]),
                          (0.85 * imshape[1], 0.99 * imshape[0])]], dtype = np.int32)
    return vertices

def get_perspective_matrices(X_img):
    offset = 15
    img_size = (X_img.shape[1], X_img.shape[0])

    # Estimate the coordinates of object of interest inside the image.
    src = np.float32(get_mask_coord(X_img.shape))
    dst = np.float32([[offset, img_size[1]], [offset, 0], [img_size[0] - offset, 0], 
                      [img_size[0] - offset, img_size[1]]])
    
    perspective_matrix = cv2.getPerspectiveTransform(src, dst)
    return perspective_matrix

def perspective_transform(img_path,name):
    X_img = cv2.imread(img_path)
    folder = os.path.dirname(img_path)
    # Doing only for one type of example
    perspective_matrix = get_perspective_matrices(X_img)
    warped_img = cv2.warpPerspective(X_img, perspective_matrix,
                                     (X_img.shape[1], X_img.shape[0]),
                                     flags = cv2.INTER_LINEAR)
    newname = name+'_1.png'
    cv2.imwrite('%s'%os.path.join(folder,newname),warped_img)
    print newname

# Produce each image at scaling of 90%, 75% and 60% of original image.

def main(args):
    images = os.listdir(IMDIR)
    for image in images:
        image_path = os.path.join(IMDIR,image)
        label_path = os.path.join(LBDIR,image)
        print image_path
        print label_path
        name = image[:-4]
        perspective_transform(image_path,name)
        perspective_transform(label_path,name)
        # print image_path
        # print label_path
    # print filenames
    # img1 = cv2.imread(img)
    
    # perspective_img = crop(img,260,200)
    # cv2.imwrite('/home/ubuntu/Desktop/testaug/1_2.png',perspective_img)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--inputim_dir',type = str,default=IMDIR ,help='Directory with original images.')
    parser.add_argument('--inputlb_dir',type = str,default = LBDIR ,help='Directory with label images.')
    # parser.add_argument('--time',type=int, help='How many time do you want to resize')
    return parser.parse_args(argv)
if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
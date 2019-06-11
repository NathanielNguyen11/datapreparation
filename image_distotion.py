import numpy as np
import cv2
from scipy.ndimage.interpolation import map_coordinates
from scipy.ndimage.filters import gaussian_filter
import matplotlib.pyplot as plt
import sys
import argparse
import os

IM = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/image'
LB = '/media/ubuntu/Quang/challenge/liver/CHAOS/CT/experi/train/300x3001/label'
def elastic_transform(image, alpha, sigma, alpha_affine, random_state=None):
    """Elastic deformation of images as described in [Simard2003]_ (with modifications).
    .. [Simard2003] Simard, Steinkraus and Platt, "Best Practices for
         Convolutional Neural Networks applied to Visual Document Analysis", in
         Proc. of the International Conference on Document Analysis and
         Recognition, 2003.

     Based on https://gist.github.com/erniejunior/601cdf56d2b424757de5
    """
    if random_state is None:
        random_state = np.random.RandomState(None)

    shape = image.shape
    shape_size = shape[:2]
    
    # Random affine
    center_square = np.float32(shape_size) // 2
    square_size = min(shape_size) // 3
    pts1 = np.float32([center_square + square_size, [center_square[0]+square_size, center_square[1]-square_size], center_square - square_size])
    pts2 = pts1 + random_state.uniform(-alpha_affine, alpha_affine, size=pts1.shape).astype(np.float32)
    M = cv2.getAffineTransform(pts1, pts2)
    image = cv2.warpAffine(image, M, shape_size[::-1], borderMode=cv2.BORDER_REFLECT_101)

    dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma) * alpha
    dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigma) * alpha
    dz = np.zeros_like(dx)

    x, y, z = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]), np.arange(shape[2]))
    indices = np.reshape(y+dy, (-1, 1)), np.reshape(x+dx, (-1, 1)), np.reshape(z, (-1, 1))

    return map_coordinates(image, indices, order=1, mode='reflect').reshape(shape)


def parse_arguments(argv):
	parser = argparse. ArgumentParser()

	parser.add_argument('--im_dir', type = str,default=IM, help='Directory with original label image')
    # parser.add_argument('--lb_dir', type = str,default=LB, help='Directory with original label image')
	parser.add_argument('--lb_dir', type = str,default=LB, help='Directory with original label image')

	return parser.parse_args(argv)

def main(args):

    a=0
    rootdir= os.path.expanduser(args.im_dir)
    rootdir1= os.path.expanduser(args.lb_dir)
    list_files = os.listdir(rootdir)
    number_files=len(list_files)
    
    for filename in os.listdir(rootdir):
        file0 = os.path.join(rootdir,filename)
        file1 = os.path.join(rootdir1,filename)
        filename1 = filename[:-4]
        im = cv2.imread(file0,0)
        im_mask =cv2.imread(file1,0)
        im_merge = np.concatenate((im[...,None], im_mask[...,None]), axis=2)
        im_merge_t = elastic_transform(im_merge, im_merge.shape[1] * 0.02, im_merge.shape[1] * 0.01, im_merge.shape[1] * 0.02)
        im_t = im_merge_t[...,0]
        im_mask_t = im_merge_t[...,1]
        cv2.imwrite(os.path.join(rootdir, filename1 + 'd.png'),np.r_[im_t])#image
        cv2.imwrite(os.path.join(rootdir1, filename1 + 'd.png'),np.r_[im_mask_t])#label
		# plt.figure(figsize = (16,14))
		# plt.imshow(np.c_[np.r_[im], np.r_[im_t]], cmap='gray')
		# plt.show()
        a=a+1
        print ('success in image number/total images: %d/%d'%(a, number_files))

if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))
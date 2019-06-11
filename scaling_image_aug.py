import tensorflow as tf
import numpy as np
import cv2
import os
import sys
def central_scale_images(X_imgs, scales):
    # Various settings needed for Tensorflow operation
    boxes = np.zeros((len(scales), 4), dtype = np.float32)
    for index, scale in enumerate(scales):
        x1 = y1 = 0.5 - 0.5 * scale # To scale centrally
        x2 = y2 = 0.5 + 0.5 * scale
        boxes[index] = np.array([y1, x1, y2, x2], dtype = np.float32)
    box_ind = np.zeros((len(scales)), dtype = np.int32)
    crop_size = np.array([288, 384], dtype = np.int32)
    
    X_scale_data = []
    tf.reset_default_graph()
    X = tf.placeholder(tf.int8, shape = (1, 288, 384, 3))
    # Define Tensorflow operation for all scales but only one base image at a time
    tf_img = tf.image.crop_and_resize(X, boxes, box_ind, crop_size)
    # print ('aaaaaaaaaaaaaaaaaaa',tf_img)
    img = tf.image.encode_jpeg(tf_img, format='rgb', quality=100)
    with tf.Session() as sess:
        a= img.eval()
        
    
    # X_scale_data = np.array(X_scale_data, dtype = np.float32)
    return a
	
# Produce each image at scaling of 90%, 75% and 60% of original image.
if __name__ == '__main__':
    img='/home/ubuntu/Desktop/testaug/1.png'
    X_imgs = cv2.imread(img)
    scaled_imgs = central_scale_images(X_imgs, [0.90, 0.75, 0.60])
    cv2.imwrite('/home/ubuntu/Desktop/testaug/1_2.png',scaled_imgs)

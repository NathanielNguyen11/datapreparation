import numpy as np
import random
import cv2

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
def main():
    image = cv2.imread('/home/ubuntu/Desktop/face_data/Quang/0021_0.png') # Only for grayscale image
    noise_img = sp_noise(image,0.035)
    cv2.imwrite('/home/ubuntu/Desktop/sp_noise.jpg', noise_img)
if __name__ == '__main__':
    main()
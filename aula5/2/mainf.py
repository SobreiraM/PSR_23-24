#!/usr/bin/env python3
#shebang line

#function descriptions...

#import modules
from time import time, sleep
from collections import namedtuple
from math import sqrt
import colorama 
from colorama import Fore, Back, Style
import cv2
import argparse
import numpy as np


def main():

    parser = argparse.ArgumentParser(description='OpenCV testing...')

    parser.add_argument('-img1', type=str, help='Submit path to png file', required = True)
 
    
    args = vars(parser.parse_args())

    image_filename1 = args['img1']
    image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image
    

    #create masks
    lowerlimit = np.array([10,75,0], dtype=np.uint8) 
    upperlimit = np.array([45,125,30], dtype=np.uint8)

    mask = cv2.inRange(image1,lowerlimit,upperlimit)
    indices = np.where(mask==255)
    
    result = image1
    result[indices[0],indices[1], :] = [0,0,255] 
   
    cv2.imshow('image1', image1)  # Display the image
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(0)             # wait for a key press before proceeding


if __name__ == '__main__':
    main()
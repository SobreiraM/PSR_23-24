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
import numpy

def main():

    parser = argparse.ArgumentParser(description='OpenCV testing...')

    parser.add_argument('-img1', type=str, help='Submit path to png file', required = True)
 
    
    args = vars(parser.parse_args())

    image_filename1 = args['img1']
    image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image
    image_gray = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    retval, image_thresholded1 = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)

    for

    cv2.imshow('window1', image_thresholded1)  # Display the image
    cv2.waitKey(0)             # wait for a key press before proceeding

    cv2.imshow('window2', image_thresholded2)  # Display the image
    cv2.waitKey(0)             # wait for a key press before proceeding

    print(image_thresholded1.dtype)
    print(image_thresholded2.dtype)
    
   


if __name__ == '__main__':
    main()
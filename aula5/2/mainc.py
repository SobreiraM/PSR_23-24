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

def main():

    parser = argparse.ArgumentParser(description='OpenCV testing...')

    parser.add_argument('-img1', type=str, help='Submit path to png file', required = True)
 
    
    args = vars(parser.parse_args())

    image_filename1 = args['img1']
    image_rgb = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image
    
    image_b, image_g, image_r = cv2.split(image_rgb) 

    retval, image_b_thresholded = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    retval, image_g_thresholded = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    retval, image_r_thresholded = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)


    image_rgb_thresholded = cv2.merge([image_b_thresholded, image_g_thresholded, image_r_thresholded]) 

    cv2.imshow('image_rgb', image_rgb)  # Display the image
    cv2.imshow('image_rgb_thresholded', image_rgb_thresholded)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()
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
from GetLimits import Get_Limits

def main():

    parser = argparse.ArgumentParser(description='OpenCV testing...')

    parser.add_argument('-img1', type=str, help='Submit path to png file', required = True)
 
    
    args = vars(parser.parse_args())

    image_filename1 = args['img1']
    image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image
    hsv_image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)

    #create masks
    green = [0,128,0]
    lowerlimit, upperlimit = Get_Limits(green)
    #lowerlimit = np.array([45,170,20]) 
    #upperlimit = np.array([70,255,255])

    mask = cv2.inRange(hsv_image,lowerlimit,upperlimit)
    result = cv2.bitwise_and(hsv_image,hsv_image, mask=mask)
   
    cv2.imshow('image1', image1)  # Display the image
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(0)             # wait for a key press before proceeding


if __name__ == '__main__':
    main()